from fasthtml.common import *

from ..components.app_logo import AppLogo
from ..components.app_page import AppPage
from ..components.app_link import AppLink
from ..components.app_lists import GameList
from ..components.app_scroll_arrow import AppScrollArrow
from ..supported_games import SUPPORTED_GAMES


def Home(session):
    return AppPage(
        AppScrollArrow(),
        Div(
            Div(
                AppLogo(cls="w-4/5"),
                P(
                    "Your Games, Your Stats",
                    cls="italic font-light",
                ),
                A(
                    Img(
                        src="https://community.akamai.steamstatic.com/public/images/signinthroughsteam/sits_01.png",
                        cls="animate-pulse shadow-md dark:shadow-none hover:shadow-xl dark:hover:shadow-none  transition-shadow",
                    ),
                    href="/signin/steam",
                    cls="mt-4",
                ),
                Script(
                    code="""
                    // this function will hide the menu until the scrollThreshold is hit
                    function updateMenu() {
                        const appMenu = document.getElementById("AppMenu");
                        const curScroll = document.documentElement.scrollTop || document.body.scrollTop;
                        const scrollThreshold = 150.0;

                        if (curScroll < scrollThreshold) {
                            if(!appMenu.classList.contains("hidden")) {
                                appMenu.classList.add("hidden");
                            }
                        } else {
                            appMenu.classList.remove("hidden");
                        }
                    }

                    addEventListener("load", updateMenu);
                    addEventListener("scroll", updateMenu);
                """
                ),
                cls="h-screen text-center flex flex-col justify-center items-center",
            ),
            Div(
                Div(
                    H2(
                        "Game ",
                        Span("Dashboard", cls="text-primary"),
                        cls="text-3xl font-black drop-shadow-md",
                    ),
                    P("Quickly access stats for any of your favorite Steam games!"),
                    cls="space-y-4",
                ),
                Div(
                    H2(
                        "All of ",
                        Span("Your", cls="text-primary"),
                        "Stats",
                        cls="text-3xl font-black drop-shadow-md",
                    ),
                    P(
                        "Each game is packed with statistics that reflect your time playing the game!"
                    ),
                    cls="space-y-4",
                ),
                Div(
                    H2(
                        Span("Expanding", cls="text-primary"),
                        " Support",
                        cls="text-3xl font-black drop-shadow-md",
                    ),
                    P(
                        "Custom supported games showcase your stats in unique, themed ways!"
                    ),
                    cls="space-y-4",
                ),
                Div(
                    H2(
                        "Supported ",
                        Span("Games", cls="text-primary"),
                        cls="text-3xl font-black drop-shadow-md",
                    ),
                    P(
                        "Dont't see the game you love? ",
                        AppLink(
                            "Request it!",
                            href="/feedback?reason=Game Request",
                        ),
                    ),
                    GameList(SUPPORTED_GAMES),
                    cls="space-y-4",
                ),
                cls="space-y-24 text-center",
            ),
            cls="container mx-auto px-4",
        ),
        padding="pt-24 pb-12",
        menu_starts_hidden=True,
        session=session,
    )
