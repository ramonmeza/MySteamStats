from fasthtml.common import *

from .app_menu import AppMenu


def AppPage(
    *content,
    steamid: int = None,
    app_name: str = "MySteamStats",
    title: str = "Your Games, Your Stats",
    background: str = None,
    margin: str = "mt-20 mb-12",
):
    return (
        Title(f"{app_name}: {title}"),
        Body(
            AppMenu(steamid=steamid),
            *content,
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css",
            ),
            Script(
                src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/js/all.min.js"
            ),
            cls=(
                f"{margin} bg-app-bg dark:bg-app-dark-bg text-app-text dark:text-app-dark-text"
                + (
                    f" bg-[url('{background}')] bg-fixed bg-cover bg-center"
                    if background
                    else ""
                )
            ),
        ),
    )
