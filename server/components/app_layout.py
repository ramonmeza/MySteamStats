from fasthtml.common import *

from ..components.app_scroll_arrow import AppScrollArrow


def AppLayout(
    *content,
    title: str = "MySteamStats: Your Games, Your Stats",
    navigation_arrow: bool = False,
):
    return (
        Title(title),
        Body(
            *content,
            AppScrollArrow() if navigation_arrow else None,
            (
                Script(src="/public/js/components/appScrollArrow.js")
                if navigation_arrow
                else None
            ),
            cls=f"min-w-screen min-h-screen bg-app-background text-app-text-main cursor-default pb-12 overflow-x-hidden",
        ),
    )
