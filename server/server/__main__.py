import fasthtml.common as fh
import os
import requests_cache
import typing

from fasthtml import FastHTML

from .authentication import user_auth_before, SteamAuth
from .errors import exception_handlers
from .pages.dashboard import Dashboard
from .pages.landing import Landing
from .pages.signin import SignIn
from .strings import *
from .toasts import set_toast, handle_toasts
from .urls import *


# create cache for all requests
requests_cache.install_cache("requests_cache")

# routes under skip parameter will be public.
# all other routes require authentication to access.
beforeware = [
    fh.Beforeware(
        user_auth_before,
        skip=[
            r"/favicon\.ico",
            r"/static/.*",
            r".*\.css",
            r".*\.js",
            "/",
            r"/signin",
            r"/signin/.*",
            r"/auth/.*",
        ],
    ),
    fh.Beforeware(handle_toasts),
]


# define app and routes
app: FastHTML = FastHTML(
    debug=True if os.getenv("ENABLE_DEBUG", "false").lower() == "true" else False,
    before=beforeware,
    exception_handlers=exception_handlers,
    hdrs=(fh.Script(src=TAILWINDCSS_CDN),),
    routes=[fh.Mount("/static", app=fh.StaticFiles(directory="static"), name="static")],
    cls="bg-gray-200",
)
rt: typing.Callable = app.route
fh.setup_toasts(app)


@rt("/")
async def get(session):
    # signed in users goto dashboard
    if session.get("auth", None) is not None:
        return fh.RedirectResponse("/dashboard", status_code=303)

    # if not signed in, goto landing page
    return Landing()


@rt("/signin")
async def get(session):
    # signin page shows all methods to login
    # in this case, only through steam (for now)
    return SignIn()


@rt("/signin/steam")
async def get():
    # hand-off authentication to steam
    return SteamAuth.authorize(callback_url=f"{os.getenv('HOST_URL')}/auth/steam")


@rt("/signout")
async def get(session):
    # reset the session auth key to None, effectively closing the active session
    session["auth"] = None
    set_toast(session, "success", SUCCESSFUL_SIGNOUT)
    return fh.RedirectResponse("/", status_code=303)


@rt("/auth/steam")
async def get(request: fh.Request, session):
    # this is the callback url that steam redirects to after authentication.
    # here we need to validate the response and get the user's steam ID, which we save into the session
    session["auth"] = SteamAuth.validate_authorization(request)

    if session.get("auth", None) is None:
        set_toast(session, "error", UNSUCCESSFUL_SIGNIN)
        return fh.RedirectResponse("/", status_code=303)
    else:
        set_toast(session, "success", SUCCESSFUL_SIGNIN)
        return fh.RedirectResponse("/dashboard", status_code=303)


@rt("/dashboard")
async def get(session):
    # dashboard shows a list of games
    steam_id = session.get("auth")
    return Dashboard(steam_api_key=os.getenv("STEAM_SECRET"), steam_id=steam_id)


@rt("/stats/{app_id:path}")
async def get(app_id: int, session):
    return fh.Div(app_id)
