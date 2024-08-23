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
from .errors import exception_handlers
from .pages.dashboard import Dashboard
from .pages.email_form import EmailForm
from .pages.game_stats import GameStats
from .pages.home import Home
from .pages.signin import SignIn
from .toasts import set_toast, handle_toasts
from .urls import *


# create cache for all requests
requests_cache.install_cache("requests_cache")

# routes under skip parameter will be public.
# all other routes require authentication to access.
beforeware = [
    Beforeware(
        user_auth_before,
        skip=[
            r"/favicon\.ico",
            r"/static/.*",
            r".*\.css",
            r".*\.js",
            "/",
            "/feedback",
            "/request",
            "/signin",
            r"/signin/.*",
            r"/auth/.*",
            "/throw"
        ],
    ),
    Beforeware(handle_toasts),
]

# load tailwind config and set headers
ENABLE_DEBUG: bool = (
    True if os.getenv("ENABLE_DEBUG", "false").lower() == "true" else False
)
if ENABLE_DEBUG:
    with open("tailwind.config.js") as fp:
        tailwind_config_code = fp.read().replace("\n", "")
hdrs = (
    (
        Script(src="https://cdn.tailwindcss.com/3.4.5"),
        Script(code=tailwind_config_code),
    )
    if ENABLE_DEBUG
    else (
        Script(src="/static/js/tailwindcss.js"),
        Link(rel="stylesheet", href="/static/css/styles.css"),
    )
)

# define app and routes
app: FastHTML = FastHTML(
    debug=ENABLE_DEBUG,
    before=beforeware,
    exception_handlers=exception_handlers,
    hdrs=hdrs,
    cls=f"cursor-default min-w-screen min-h-screen text-textcolor1 bg-gradient-to-b from-color1 via-color2 via-30% via-color3 via-60% to-color4",
    routes=[Mount("/static", app=StaticFiles(directory="static"), name="static")],
)
rt: typing.Callable = app.route
setup_toasts(app)


@rt("/")
async def get(session):
    # signed in users goto dashboard
    if session.get("auth", None) is not None:
        return RedirectResponse("/dashboard", status_code=303)

    # if not signed in, goto home page
    return Home()


@rt("/signin")
async def get(session):
    return SignIn()


@rt("/signin/steam")
async def get():
    # hand-off authentication to steam
    return SteamAuth.authorize(callback_url=f"{os.getenv('HOST_URL')}/auth/steam")


@rt("/signout")
async def get(session):
    # reset the session auth key to None, effectively closing the active session
    session["auth"] = None
    set_toast(session, "success", "You've successfully signed out")
    return RedirectResponse("/", status_code=303)


@rt("/auth/steam")
async def get(request: Request, session):
    # this is the callback url that steam redirects to after authentication.
    # here we need to validate the response and get the user's steam ID, which we save into the session
    session["auth"] = SteamAuth.validate_authorization(request)

    if session.get("auth", None) is None:
        set_toast(session, "error", "You've failed to sign in!")
        return RedirectResponse("/", status_code=303)
    else:
        set_toast(session, "success", "You've successfully signed in")
        return RedirectResponse("/dashboard", status_code=303)


@rt("/dashboard")
async def get(session):
    steam_id = session.get("auth")
    return Dashboard(steam_api_key=os.getenv("STEAM_SECRET"), steam_id=steam_id)


@rt("/stats/{app_id:path}")
async def get(app_id: int, session):
    return GameStats(app_id)


@rt("/feedback")
async def get():
    return EmailForm("GameStats Feedback")


@rt("/request")
async def get():
    return EmailForm("GameStats Game Request")


@rt("/throw")
async def get():
    raise Exception("Butthole butter")
