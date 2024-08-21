import fasthtml.common as fh

from ..strings import *


def SignIn():
    return fh.Div(
        fh.H1(SIGNIN),
        fh.A(
            fh.Img(
                src="/static/img/steam_signin_chonky.png",
                alt=SIGNIN_THROUGH_STEAM,
            ),
            href="/signin/steam/",
        ),
    )
