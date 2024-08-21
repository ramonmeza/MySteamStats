import fasthtml.common as fh
import typing

from fasthtml import FastHTML

from .pages.dashboard import Dashboard
from .pages.landing import Landing
from .pages.signin import SignIn
from .steam_auth import SteamAuth


def user_auth_before(request: fh.Request, session):
    # authentication method, which allows access based on whether the auth parameter is set in the session
    auth = request.scope["auth"] = session.get("auth", None)

    if not auth:
        return fh.RedirectResponse("/signin", status_code=303)


# routes under skip parameter will be public.
# all other routes require authentication to access.
beforeware = fh.Beforeware(
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
)

app: FastHTML = FastHTML(
    debug=True,
    before=beforeware,
    hdrs=(fh.Script(src="https://cdn.tailwindcss.com"),),
    routes=[fh.Mount("/static", app=fh.StaticFiles(directory="static"), name="static")],
    cls="bg-gray-200",
)
rt: typing.Callable = app.route


@rt("/")
async def get(session):
    # signed in users goto dashboard
    if session.get("auth", None) is not None:
        return fh.RedirectResponse("/dashboard", status_code=303)

    # if not signed in, goto landing page
    return Landing()


@rt("/signin")
async def get():
    # signin page shows all methods to login
    # in this case, only through steam (for now)
    return SignIn()


@rt("/signin/steam")
async def get():
    # hand-off authentication to steam
    return SteamAuth.authorize(callback_url="http://localhost:8000/auth/steam")


@rt("/signout")
async def get(session):
    # reset the session auth key to None, effectively closing the active session
    session["auth"] = None
    return fh.RedirectResponse("/", status_code=303)


@rt("/auth/steam")
async def get(request: fh.Request, session):
    # this is the callback url that steam redirects to after authentication.
    # here we need to validate the response and get the user's steam ID, which we save into the session
    session["auth"] = SteamAuth.validate_authorization(request)

    # redirect users to the homepage, which should redirect them to the dashboard
    return fh.RedirectResponse("/", status_code=303)


@rt("/dashboard")
async def get(session):
    # dashboard shows a list of games
    return Dashboard()
