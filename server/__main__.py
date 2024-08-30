import os
import requests_cache
import typing

from fasthtml.common import (
    Beforeware,
    Div,
    FastHTML,
    I,
    Link,
    Meta,
    Mount,
    P,
    RedirectResponse,
    Request,
    Response,
    Script,
    setup_toasts,
    StaticFiles,
)


from .authentication import authenticate_admin, SteamAuth, user_auth_before
from .db import delete_feedback, get_all_feedback
from .components.app_lists import FeedbackList
from .pages.admin_login import AdminLogin
from .pages.admin_panel import AdminPanel
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
    "ADMIN_EMAIL",
    "ADMIN_PASSWORD",
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
            r"/public/.*",
            "/",
            "/feedback",
            "/privacy_policy",
            r"^/signin(/.*)?$",
            r"^/admin(/.*)?$",
            r"^/auth(/.*)?$",
        ],
    ),
    Beforeware(handle_toasts),
    Beforeware(authenticate_admin, skip=[r"^(?!/admin(/.*)?$).*$"]),
]


# load tailwind config and set headers
if ENABLE_DEBUG:
    with open("tailwind.config.js") as fp:
        tailwind_config_code = fp.read().replace("\n", "")
hdrs = (
    (
        Meta(
            name="description",
            content="Quickly access stats for any of your favorite Steam games!",
        ),
        Link(rel="icon", type="image/x-icon", href="/public/img/favicon.ico"),
        Script(src="https://cdn.tailwindcss.com"),
        Script(code=tailwind_config_code),
    )
    if ENABLE_DEBUG
    else (
        Meta(
            name="description",
            content="Quickly access stats for any of your favorite Steam games!",
        ),
        Link(rel="icon", type="image/x-icon", href="/public/img/favicon.ico"),
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
    player = session.get("player", None)
    isAdmin = session.get("isAdmin", None)

    if player is not None and not isAdmin:
        return RedirectResponse("/dashboard", status_code=303)

    elif isAdmin:
        return RedirectResponse("/admin/panel", status_code=303)

    # if not signed in, goto home page
    return Home(session=session)


@rt("/signin/steam")
async def get():
    # hand-off authentication to steam
    callback_url = os.getenv("HOST_URL")
    return SteamAuth.authorize(callback_url=f"{callback_url}/auth/steam")


@rt("/signin/admin")
async def get(session):
    return AdminLogin(session)


@rt("/signout")
async def get(session):
    # reset the session auth key to None, effectively closing the active session
    session.clear()
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
        if form["email"] == os.getenv("ADMIN_EMAIL") and form["password"] == os.getenv(
            "ADMIN_PASSWORD"
        ):
            session["isAdmin"] = True
            set_toast(session, "success", "You've signed in as Admin!")
            return RedirectResponse("/admin/panel", status_code=303)
        else:
            raise Exception
    except Exception as e:
        session["isAdmin"] = None
        set_toast(session, "error", "You've failed to sign in!")
        return RedirectResponse("/", status_code=303)


@rt("/admin/panel")
async def get(session):
    return AdminPanel(session=session)


@rt("/admin/feedback")
async def get():
    feedback = await get_all_feedback()
    return (FeedbackList(feedback),)


@rt("/admin/feedback")
async def delete(request: Request):
    try:
        id = request.query_params.get("id")
        reason = request.query_params.get("reason")
        success = await delete_feedback(id, reason)

        if success:
            return Response(status_code=200)

    except Exception as e:
        return Div(
            I(cls="fa-solid fa-exclamation-triangle text-error"),
            P("There was an unexpected error!"),
            P(str(e), cls="text-xs text-mid"),
            cls="text-center",
        )


@rt("/dashboard")
async def get(session):
    return Dashboard(session=session, steam_api_key=os.getenv("STEAM_SECRET"))


@rt("/stats/{appid:path}")
async def get(appid: int, session):
    if appid not in [game["appid"] for game in SUPPORTED_GAMES]:
        set_toast(
            session,
            "warning",
            "This game is not officially supported and my display incorrectly. If you'd like, you can request official support for it.",
        )
        handle_toasts(session)

    return GameStats(
        session=session, steam_api_key=os.getenv("STEAM_SECRET"), appid=appid
    )


@rt("/feedback")
async def get(request, session):
    return FeedbackForm(
        session=session,
        reason=(
            request.query_params["reason"] if "reason" in request.query_params else None
        ),
    )


@rt("/feedback")
async def post(request):
    form = await request.form()
    return await FeedbackSubmitted(form)


@rt("/privacy_policy")
async def get(session):
    return PrivacyPolicy(session=session)
