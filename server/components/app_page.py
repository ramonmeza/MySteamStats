from fasthtml.common import *

from .app_menu import AppMenu


def AppPage(
    *content,
    player: dict = None,
    app_name: str = "MySteamStats",
    title: str = "Your Games, Your Stats",
    background: str = None,
    margin: str = "mt-24 mb-12",
    menu_starts_hidden: bool = False
):
    return (
        Title(f"{app_name}: {title}"),
        Body(
            AppMenu(player=player, hidden=menu_starts_hidden),
            *content,
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css",
            ),
            Script(
                src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/js/all.min.js"
            ),
            cls=(
                f"{margin} cursor-default bg-light dark:bg-dark text-dark dark:text-light"
                + (
                    f" bg-[url('{background}')] bg-fixed bg-cover bg-[center_top_4rem]"
                    if background
                    else ""
                )
            ),
        ),
    )
