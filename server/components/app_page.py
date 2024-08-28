from fasthtml.common import *

from .app_link import AppLink
from .app_menu import AppMenu


def AppPage(
    *content,
    player: dict = None,
    app_name: str = "MySteamStats",
    title: str = "Your Games, Your Stats",
    background: str = None,
    padding: str = "pt-24 px-4",
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
                P("© MySteamStats. All rights reserved."),
                P(
                    "All trademarks are property of their respective owners in the US and other countries.",
                ),
                P(
                    "This site is not associated with ",
                    AppLink(
                        "Valve Corp.",
                        href="https://www.valvesoftware.com/en/",
                        target="_blank",
                    ),
                ),
                Div(AppLink("Privacy Policy", href="/privacy_policy"), cls="py-2"),
                cls="mt-auto pt-16 h-full text-center text-xs",
            ),
            Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css",
            ),
            Script(
                src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/js/all.min.js"
            ),
            cls=(
                f"{padding} relative font-['Exo'] cursor-default min-w-screen min-h-screen flex flex-col bg-light dark:bg-dark text-dark dark:text-light"
                + (
                    f" bg-[url('{background}')] bg-fixed bg-cover bg-[center_top_4rem]"
                    if background
                    else ""
                )
            ),
        ),
    )
