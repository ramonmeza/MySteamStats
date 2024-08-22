from fasthtml.common import *


def SignIn():
    return (
        Title("GameStats: Sign In"),
        Body(
            Div(
                Div(
                    H1("Sign In", cls="text-5xl font-bold"),
                    P(
                        "Log in ",
                        Strong("securely"),
                        " using Steam",
                        cls="text-lg italic",
                    ),
                    A(
                        Img(
                            src="/static/img/steam_signin_chonky.png",
                            alt="Sign in through STEAM",
                            cls="m-4 w-max mx-auto shadow hover:shadow-xl transition-shadow",
                        ),
                        href="/signin/steam/",
                    ),
                    cls="w-max h-max mx-auto rounded-lg px-4 py-6 text-white bg-gray-400",
                ),
                cls="min-w-screen min-h-screen flex flex-col justify-center text-center",
            ),
            cls="min-w-screen min-h-screen bg-gray-800",
        ),
    )
