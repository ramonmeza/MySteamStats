from fasthtml.common import A, Body, Div, H1, H2, Img, P, Script, Title

from ..components.app_button import AppButton
from ..components.divider import Divider
from ..components.down_arrow import DownArrow
from ..components.game_card import GameCard
from ..pages.site_footer import SiteFooter
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
                    H1(f"{SITE_NAME}", cls="text-4xl font-bold"),
                    P("Your Games, Your Stats", cls="text-lg italic"),
                    AppButton(content="Get Started", href="/signin", pulse=True),
                    cls="grid grid-rows-3 h-max place-items-center",
                ),
                cls="min-w-screen min-h-screen flex flex-col justify-center text-center",
            ),
            Divider(),
            Div(
                Div(
                    Div(
                        H2("Stats Dashboard", cls="text-xl text-header"),
                        P(
                            "Quickly access your library of games via Steam",
                            cls="italic",
                        ),
                    ),
                    Div(
                        H2("Game Stats", cls="text-xl text-header"),
                        P(
                            "Access hundreds of easily searchable statstical data points",
                            cls="italic",
                        ),
                    ),
                    Div(
                        H2("Constantly Expanding Library", cls="text-xl text-header"),
                        P(
                            "We are constantly adding new games and are willing to take your game ",
                            A(
                                "requests!",
                                href="/request",
                                cls="text-textlink hover:text-textlinkhover duration-300",
                            ),
                            cls="italic",
                        ),
                    ),
                    cls="container mx-auto text-center px-4 py-12 space-y-12",
                ),
                cls="min-w-screen",
            ),
            Divider(),
            Div(
                H2("Supported Games", cls="pt-8 text-2xl text-header"),
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
                    "Powered by",
                    cls="italic text-textalt mb-2",
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
            SiteFooter(),
            Script(src="/public/js/scroll.js"),
        ),
    )
