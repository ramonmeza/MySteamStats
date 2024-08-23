from fasthtml.common import *


def SignIn():
    return (
        Title("GameStats: Sign In"),
        Body(
            Div(
                Div(
                    H1("Sign In to GameStats", cls="text-3xl"),
                    P(
                        "This site utilizes the Steam Web API. You must log in using your Steam account to access all of GameStats' features. Simply press the button below to get started!"
                    ),
                    A(
                        Img(
                            src="/static/img/steam_signin_chonky.png",
                            alt="Sign in through STEAM",
                            cls="shadow hover:shadow-lg transition-shadow mx-auto w-max",
                        ),
                        href="/signin/steam/",
                    ),
                    cls="flex flex-col w-96 bg-color2 rounded-lg shadow p-10 mx-auto text-center space-y-4",
                ),
                cls="min-w-screen min-h-screen flex flex-col justify-center",
            ),
            Div(
                P(
                    "We'd love to hear your",
                    A(
                        "feedback!",
                        href="/feedback",
                        cls="text-textcolor2 hover:text-textcolor3 duration-300",
                    ),
                ),
                P(
                    "Copyright © 2024 GameStats. All rights reserved.",
                    cls="text-color2 text-sm",
                ),
                cls="absolute bottom-6 container text-center",
            ),
            cls=f"text-textcolor1 bg-gradient-to-b from-color1 via-color2 via-30% via-color3 via-60% to-color4",
        ),
    )
