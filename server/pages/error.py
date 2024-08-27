from fasthtml.common import *

from ..components.app_link import AppLink
from ..components.app_page import AppPage


def Error(request, exception):
    # @todo: pass request to feedback form
    return AppPage(
        Div(
            I(cls="fa-solid fa-face-frown h-32 w-32 text-primary"),
            H1(str(exception), cls="text-3xl"),
            P(
                "We're sorry you've encountered an error. Feel free to ",
                AppLink(
                    "report the issue",
                    href="/feedback?reason=App Issue",
                ),
                " to us.",
            ),
            cls="text-center mt-56",
        ),
        title=str(exception),
    )
