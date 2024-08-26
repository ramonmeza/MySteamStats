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
from .pages.feedback_form import FeedbackForm
from .pages.game_stats import GameStats
from .pages.home import Home
from .strings import *
from .toasts import set_toast, handle_toasts
from .urls import *


if os.getenv("HOST_URL", None) is None:
    print("You must define the environment variable HOST_URL")
    exit(-1)

if not os.getenv("STEAM_SECRET", None):
    print("You must define the environment variable STEAM_SECRET")
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
    if session.get("auth", None) is not None:
        return RedirectResponse("/dashboard", status_code=303)

    # if not signed in, goto home page
    return Home()


@rt("/signin/steam")
async def get():
    # hand-off authentication to steam
    callback_url = os.getenv("HOST_URL")
    return SteamAuth.authorize(callback_url=f"{callback_url}/auth/steam")


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
    steam_id = session.get("auth")
    return GameStats(os.getenv("STEAM_SECRET"), steam_id, app_id)


@rt("/feedback")
async def get(request):
    return FeedbackForm(reason=request.query_params["reason"])
