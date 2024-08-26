from fasthtml.common import *

from ..components.app_scroll_arrow import AppScrollArrow


def AppLayout(*content, title: str = "MySteamStats: Your Games, Your Stats"):
    return (
        Title(title),
        Body(
            *content,
            AppScrollArrow(),
            Script(src="/public/js/components/appScrollArrow.js"),
            cls=f"min-w-screen min-h-screen bg-app-background text-app-text-main cursor-default pb-12",
        ),
    )
