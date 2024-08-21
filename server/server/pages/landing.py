import fasthtml.common as fh

from ..strings import *


def Landing():
    return fh.Div(
        fh.H1(WELCOME),
        fh.P(TAGLINE),
        (
            fh.A(
                SIGNIN,
                href="/signin",
            )
        ),
    )
