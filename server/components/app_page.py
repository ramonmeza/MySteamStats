from fasthtml.common import *

from .app_link import AppLink
from .app_menu import AppMenu


def AppPage(
    *content,
    player: dict = None,
    app_name: str = "MySteamStats",
    title: str = "Your Games, Your Stats",
    background: str = None,
    margin: str = "mt-24 mb-12",
    menu_starts_hidden: bool = False,
):
    font = Link(
        rel="stylesheet",
        href="https://fonts.googleapis.com/css2?family=Exo:ital,wght@0,100..900;1,100..900&display=swap",
    )
    return (
        Title(f"{app_name}: {title}"),
        Body(
            font,
            AppMenu(player=player, hidden=menu_starts_hidden),
            *content,
            Footer(
                Div(
                    P("© MySteamStats. All rights reserved."),
                    P(
                        "All trademarks are property of their respective owners in the US and other countries.",
                    ),
                    P(
                        "This site is not associated with ",
                        AppLink(
                            "Valve Corp.", href="https://www.valvesoftware.com/en/"
                        ),
                    ),
                    Div(AppLink("Privacy Policy", href="/privacy_policy")),
                    cls="container mx-auto px-4 mt-8 text-center text-xs",
                )
            ),
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css",
            ),
            Script(
                src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/js/all.min.js"
            ),
            cls=(
                f"{margin} font-['Exo'] cursor-default bg-light dark:bg-dark text-dark dark:text-light"
                + (
                    f" bg-[url('{background}')] bg-fixed bg-cover bg-[center_top_4rem]"
                    if background
                    else ""
                )
            ),
        ),
    )
