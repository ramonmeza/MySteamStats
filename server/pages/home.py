from fasthtml.common import A, Body, Button, Div, H1, H2, Img, P, Script, Title

from ..components.divider import Divider
from ..components.down_arrow import DownArrow
from ..components.game_card import GameCard
from ..strings import *
from ..supported_games import SUPPORTED_GAMES


def Home():
    return (
        Title(f"{SITE_NAME}: Your Games, Your Stats"),
        Body(
            DownArrow(
                onclick="clickScrollArrow();",
                id="PageArrow",
                cls="fixed bottom-6 left-0 right-0 cursor-pointer duration-500",
            ),
            Div(
                Div(
                    H1(f"{SITE_NAME}", cls="text-6xl font-bold"),
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
                Div(
                    Div(
                        H2("Stats Dashboard", cls="text-3xl"),
                        P(
                            "Quickly access your library of games via Steam",
                            cls="italic",
                        ),
                    ),
                    Div(
                        H2("Game Stats", cls="text-3xl"),
                        P(
                            "Access hundreds of easily searchable statstical data points",
                            cls="italic",
                        ),
                    ),
                    Div(
                        H2("Constantly Expanding Library", cls="text-3xl"),
                        P(
                            "We are constantly adding new games and are willing to take your game ",
                            A(
                                "requests!",
                                href="/request",
                                cls="text-textcolor2 hover:text-textcolor3 duration-300",
                            ),
                            cls="italic",
                        ),
                    ),
                    cls="container mx-auto text-center py-12 space-y-12",
                ),
                cls="min-w-screen",
            ),
            Divider(),
            Div(
                H2("Supported Games", cls="pt-8 text-3xl"),
                Div(
                    *[
                        GameCard(app_id, game_name)
                        for app_id, game_name in SUPPORTED_GAMES.items()
                    ],
                    cls="grid grid-cols-1 px-4 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 place-items-center",
                ),
                cls="pb-8 container mx-auto text-center space-y-4",
            ),
            Div(
                P(
                    f"{SITE_NAME} is proudly powered by",
                    cls="italic text-textcolor3 mb-2",
                ),
                Div(
                    A(
                        Img(src="/public/img/fasthtml.svg", cls="h-full"),
                        href="https://www.fastht.ml/",
                        target="_blank",
                        cls="shadow hover:shadow-lg transition-shadow",
                    ),
                    A(
                        Img(src="/public/img/python.svg", cls="h-full"),
                        href="https://www.python.org/",
                        target="_blank",
                        cls="shadow hover:shadow-lg transition-shadow my-auto h-full",
                    ),
                    cls="flex items-center space-x-8 justify-center h-12",
                ),
                cls="container mx-auto text-center",
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
                    COPYRIGHT_NOTICE,
                    cls="text-textcolor3 text-sm",
                ),
                cls="pt-4 pb-12 container mx-auto text-center",
            ),
            Script(src="/public/js/scroll.js"),
        ),
    )
