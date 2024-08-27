from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_page import AppPage
from ..components.app_lists import GameList
from ..components.app_scroll_arrow import AppScrollArrow
from ..supported_games import SUPPORTED_GAMES


def Home():
    return AppPage(
        AppScrollArrow(),
        Div(
            Div(
                H1("MySteamStats", cls="text-4xl font-bold"),
                P(
                    "Your Games, Your Stats",
                    cls="italic text-app-accent dark:text-app-dark-accent",
                ),
                A(
                    AppButton("Get Started"),
                    href="/signin/steam",
                ),
                Script(
                    code="""
                    // this function will hide the menu until the scrollThreshold is hit
                    function updateMenu() {
                        const appMenu = document.getElementById("AppMenu");
                        const curScroll = document.documentElement.scrollTop || document.body.scrollTop;
                        const scrollThreshold = 150.0;

                        if (curScroll < scrollThreshold) {
                            appMenu.classList.add("hidden");
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
                        Span(
                            "Dashboard", cls="text-app-accent dark:text-app-dark-accent"
                        ),
                        cls="text-3xl font-black",
                    ),
                    P("Quickly access stats for any of your favorite Steam games!"),
                    cls="space-y-4",
                ),
                Div(
                    H2(
                        "All of ",
                        Span("Your", cls="text-app-accent dark:text-app-dark-accent"),
                        "Stats",
                        cls="text-3xl font-black",
                    ),
                    P(
                        "Each game is packed with statistics that reflect your time playing the game!"
                    ),
                    cls="space-y-4",
                ),
                Div(
                    H2(
                        Span(
                            "Expanding", cls="text-app-accent dark:text-app-dark-accent"
                        ),
                        " Support",
                        cls="text-3xl font-black",
                    ),
                    P(
                        "Custom supported games showcase your stats in unique, themed ways!"
                    ),
                    cls="space-y-4",
                ),
                Div(
                    H2(
                        "Supported ",
                        Span("Games", cls="text-app-accent dark:text-app-dark-accent"),
                        cls="text-3xl font-black",
                    ),
                    P(
                        "Dont't see the game you love? ",
                        A(
                            "Request it!",
                            href="/feedback?reason=Game Request",
                            cls="text-app-accent dark:text-app-dark-accent hover:text-app-accent-hover dark:hover:text-app-dark-accent-hover",
                        ),
                    ),
                    GameList(SUPPORTED_GAMES),
                    cls="space-y-4",
                ),
                cls="space-y-24 text-center",
            ),
            cls="container mx-auto px-4",
        ),
        margin="mt-0 mb-12",
    )
