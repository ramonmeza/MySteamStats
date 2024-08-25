from fasthtml.common import *

from ..strings import SITE_NAME

COPYRIGHT_NOTICE = f"Copyright © 2024 {SITE_NAME}. All rights reserved."


def SiteFooter(cls: str | None = None):
    return Div(
        P(
            "We'd love to hear your",
            A(
                "feedback!",
                href="/feedback",
                cls="text-textlink hover:text-textlinkhover duration-300",
            ),
        ),
        P(
            COPYRIGHT_NOTICE,
            cls="text-textalt text-sm",
        ),
        cls=cls if cls else "pt-4 pb-12 container mx-auto text-center",
    )
