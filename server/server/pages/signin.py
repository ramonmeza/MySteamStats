import fasthtml.common as fh

from .layout import Layout


def SignIn():
    return Layout(
        "Sign In",
        children=[
            fh.Div(
                fh.H1("Sign In"),
                fh.A(
                    fh.Img(
                        src="/static/img/steam_signin_chonky.png",
                        alt="Sign in through STEAM",
                    ),
                    href="/signin/steam/",
                ),
            )
        ],
    )
