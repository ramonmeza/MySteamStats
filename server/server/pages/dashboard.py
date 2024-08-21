import fasthtml.common as fh

from ..strings import *


def Dashboard():
    return fh.Div(fh.A(SIGNOUT, href="/signout"), fh.H1(DASHBOARD))
