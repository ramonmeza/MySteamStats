from fasthtml.common import A, Body, Div, H1, Img, P, Title

from ..strings import *
from ..pages.site_footer import SiteFooter

def SignIn():
    return (
        Title(f"{SITE_NAME}: Sign In"),
        Body(
            Div(
                Div(
                    H1(f"Sign In to {SITE_NAME}", cls="text-3xl"),
                    P(
                        f"This site utilizes the Steam Web API. You must sign in using your Steam account to access all of {SITE_NAME + '\'' if SITE_NAME.lower().endswith('s') else SITE_NAME + '\'s'} features. Press the button below to get started!"
                    ),
                    A(
                        Img(
                            src="/public/img/steam_signin_chonky.png",
                            alt="Sign in through STEAM",
                            cls="shadow hover:shadow-lg transition-shadow mx-auto w-max",
                        ),
                        href="/signin/steam/",
                    ),
                    cls="flex flex-col w-96 bg-color2 rounded-lg shadow p-10 mx-auto text-center space-y-4",
                ),
                cls="min-w-screen min-h-screen flex flex-col justify-center",
            ),
            SiteFooter(
                cls="absolute bottom-6 left-0 right-0 text-center"),
            ),
        )
