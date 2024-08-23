from fasthtml.common import *
import fasthtml.svg as svg

from ..components.divider import Divider
from ..components.down_arrow import DownArrow
from ..components.game_card import GameCard
from ..supported_games import SUPPORTED_GAMES

inline_js: str = """
    function updateArrowDirection() {
        const pageArrow = document.getElementById("PageArrow");
        const currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
        let nextScroll = currentScroll + 1 + window.innerHeight;
        
        if (nextScroll >= document.body.scrollHeight) {
            // up arrow
            pageArrow.classList.add("-scale-y-100");
        } else {
            // down arrow
            pageArrow.classList.remove("-scale-y-100");
        }
    }

    addEventListener("scroll", updateArrowDirection);

    function clickScrollArrow() {
        const pageArrow = document.getElementById("PageArrow");
        const cur = document.documentElement.scrollTop || document.body.scrollTop;
        const next = cur + 1 + window.innerHeight;
        
        if (next >= document.body.scrollHeight) {
            window.scrollTo({top: 0, behavior: "smooth"});
        } else {
            window.scrollTo({top: next, behavior: "smooth"});
        }
    }
    """


def Home():
    return (
        Title("GameStats: Your Games, Your Stats"),
        Body(
            DownArrow(
                onclick="clickScrollArrow();",
                id="PageArrow",
                cls="fixed bottom-6 left-0 right-0 cursor-pointer duration-500",
            ),
            Div(
                Div(
                    H1("GameStats", cls="text-6xl font-bold"),
                    P("Your Games, Your Stats", cls="text-lg italic "),
                    Button(
                        "Get Started",
                        onclick="document.location = '/signin'",
                        cls="w-max px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover animate-pulse hover:animate-none duration-200",
                    ),
                    cls="grid grid-rows-3 h-max place-items-center",
                ),
                cls="min-w-screen min-h-screen flex flex-col justify-center text-center",
            ),
            Divider(),
            Div(
                Div(H1("features"), cls="container mx-auto"),
                cls="min-w-screen min-h-screen",
            ),
            Divider(),
            Div(
                H2("Supported Games", cls="text-3xl"),
                P(
                    "We are constantly adding new games and are willing to take your game ",
                    A(
                        "requests!",
                        href="/request",
                        cls="text-textcolor2 hover:text-textcolor3 duration-300",
                    ),
                ),
                Div(
                    *[
                        GameCard(app_id, game_name)
                        for app_id, game_name in SUPPORTED_GAMES.items()
                    ],
                    cls="grid grid-cols-1 px-4 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 place-items-center",
                ),
                cls="pt-12 pb-8 container mx-auto text-center space-y-4",
            ),
            Div(
                P(
                    "We'd love to hear your",
                    A(
                        "feedback!",
                        href="/feedback",
                        cls="text-textcolor2 hover:text-textcolor3 duration-300",
                    ),
                ),
                P(
                    "Copyright © 2024 GameStats. All rights reserved.",
                    cls="text-color2 text-sm",
                ),
                cls="py-12 container text-center",
            ),
            #  Div(
            #      P(
            #          "We'd love to hear your",
            #          A(
            #              "feedback!",
            #              href="/feedback",
            #              cls="text-blue-600 hover:text-blue-300 hover:underline duration-200",
            #          ),
            #      ),
            #      P("Copyright © 2024 GameStats. All rights reserved."),
            #      cls="min-w-screen min-h-full text-center my-10",
            #  ),
            Script(code=inline_js),
            cls=f"text-textcolor1 bg-gradient-to-b from-color1 via-color2 via-30% via-color3 via-60% to-color4",
        ),
    )

    #         Div(
    #             Div(
    #                 Div(
    #                     H2("Stats Dashboard", cls="text-2xl font-bold"),
    #                     P(
    #                         "Quickly access your library of games via Steam",
    #                         cls="italic",
    #                     ),
    #                     cls="text-left w-56",
    #                 ),
    #             ),
    #             Div(
    #                 Div(
    #                     H2("Game Stats", cls="text-2xl font-bold"),
    #                     P(
    #                         "Access hundreds of easily searchable statstical data points",
    #                         cls="italic",
    #                     ),
    #                     cls="text-right w-56 float-right",
    #                 ),
    #             ),
    #             cls="min-w-screen px-12 py-24 space-y-32 flex flex-col justify-center",
    #         ),
