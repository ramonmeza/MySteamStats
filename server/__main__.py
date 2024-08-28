import os
import requests_cache
import typing

from fasthtml.common import (
    Beforeware,
    FastHTML,
    Link,
    Mount,
    RedirectResponse,
    Request,
    Script,
    setup_toasts,
    StaticFiles,
)


from .authentication import user_auth_before, SteamAuth
from .pages.admin_login import AdminLogin
from .pages.dashboard import Dashboard
from .pages.error import Error
from .pages.feedback_form import FeedbackForm, FeedbackSubmitted
from .pages.game_stats import GameStats
from .pages.home import Home
from .pages.privacy_policy import PrivacyPolicy
from .steamapi import SteamAPI
from .supported_games import SUPPORTED_GAMES
from .toasts import set_toast, handle_toasts


# verify required environment variables are set
for ev in [
    "HOST_URL",
    "STEAM_SECRET",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_DEFAULT_REGION",
]:
    if os.getenv("HOST_URL", None) is None:
        print(f"You must define the environment variable {ev}")
        exit(-1)

ENABLE_DEBUG: bool = (
    True if os.getenv("ENABLE_DEBUG", "false").lower() == "true" else False
)


# create cache for all requests
requests_cache.install_cache("requests_cache")

# routes under skip parameter will be public.
# all other routes require authentication to access.
beforeware = [
    Beforeware(
        user_auth_before,
        skip=[
            r"/favicon\.ico",
            r"/public/.*",
            r".*\.css",
            r".*\.js",
            "/",
            "/feedback",
            "/privacy_policy",
            "/signin",
            r"/signin/.*",
            r"/auth/.*",
        ],
    ),
    Beforeware(handle_toasts),
]


# load tailwind config and set headers
if ENABLE_DEBUG:
    with open("tailwind.config.js") as fp:
        tailwind_config_code = fp.read().replace("\n", "")
hdrs = (
    (
        Link(rel="icon", type="image/x-icon", href="/public/img/favicon.ico"),
        Script(src="https://cdn.tailwindcss.com"),
        Script(code=tailwind_config_code),
    )
    if ENABLE_DEBUG
    else (
        Link(rel="icon", type="image/x-icon", href="/public/img/favicon.ico"),
        Script(src="/public/js/tailwindcss.min.js"),
        Link(rel="stylesheet", href="/public/css/styles.css"),
    )
)


# error handlers
exception_handlers = {
    500: lambda req, exc: Error(req, exc),
    404: lambda req, exc: Error(req, exc),
}


# define app and routes
app: FastHTML = FastHTML(
    debug=ENABLE_DEBUG,
    before=beforeware,
    exception_handlers=exception_handlers,
    hdrs=hdrs,
    routes=[Mount("/public", app=StaticFiles(directory="public"), name="public")],
)
rt: typing.Callable = app.route
setup_toasts(app)


@rt("/")
async def get(session):
    # signed in users goto dashboard
    if session.get("player", None) is not None:
        return RedirectResponse("/dashboard", status_code=303)

    # if not signed in, goto home page
    return Home()


@rt("/signin/steam")
async def get():
    # hand-off authentication to steam
    callback_url = os.getenv("HOST_URL")
    return SteamAuth.authorize(callback_url=f"{callback_url}/auth/steam")


@rt("/signin/admin")
async def get(session):
    return AdminLogin(player=session.get("player", None))


@rt("/signout")
async def get(session):
    # reset the session auth key to None, effectively closing the active session
    session["player"] = None
    set_toast(session, "success", "You've successfully signed out")
    return RedirectResponse("/", status_code=303)


@rt("/auth/steam")
async def get(request: Request, session):
    # this is the callback url that steam redirects to after authentication.
    # here we need to validate the response and get the user's steam ID, which we save into the session
    try:
        steamid = SteamAuth.validate_authorization(request)
        session["player"] = SteamAPI.ISteamUser.GetPlayerSummaries(
            os.getenv("STEAM_SECRET"), [steamid]
        )["response"]["players"][0]

        # this will throw if "player" doesnt exist
        assert session.get("player", None) is not None

        set_toast(session, "success", "You've successfully signed in")
        return RedirectResponse("/dashboard", status_code=303)
    except:
        session["player"] = None
        set_toast(session, "error", "You've failed to sign in!")
        return RedirectResponse("/", status_code=303)


@rt("/auth/admin")
async def post(request: Request, session):
    try:
        form = await request.form()
        set_toast(session, "success", "You've signed in as Admin!")
        return RedirectResponse("/", status_code=303)
    except Exception as e:
        set_toast(session, "error", "You've failed to sign in!")
        return RedirectResponse("/", status_code=303)


@rt("/dashboard")
async def get(session):
    player = session.get("player")
    return Dashboard(os.getenv("STEAM_SECRET"), player)


@rt("/stats/{appid:path}")
async def get(appid: int, session):
    player = session.get("player")

    if appid not in [game["appid"] for game in SUPPORTED_GAMES]:
        set_toast(
            session,
            "warning",
            "This game is not officially supported and my display incorrectly. If you'd like, you can request official support for it.",
        )
        handle_toasts(session)

    return GameStats(os.getenv("STEAM_SECRET"), player, appid)


@rt("/feedback")
async def get(request, session):
    return FeedbackForm(
        player=session.get("player", None),
        reason=(
            request.query_params["reason"] if "reason" in request.query_params else None
        ),
    )


@rt("/feedback")
async def post(request):
    form = await request.form()
    return FeedbackSubmitted(form)


@rt("/privacy_policy")
async def get(request, session):
    player = session.get("player", None)
    return PrivacyPolicy(player)
