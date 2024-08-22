from fasthtml.common import *

from ..components.game_card import GameCard
from ..supported_games import SUPPORTED_GAMES
from .layout import Layout


def Landing():
    return Layout(
        children=[
            Div(
                H1("GameStats", cls="text-4xl"),
                H2("Your Games, Your Stats", cls="text-2xl"),
                P("Quickly access all of your stats from your favorite games!"),
                H3("Supported Games", cls="text-xl"),
                Div(
                    *[
                        GameCard(app_id, game_name)
                        for app_id, game_name in SUPPORTED_GAMES.items()
                    ],
                    cls="grid grid-cols-1 p-4 gap-4 md:grid-cols-2 lg:grid-cols-4",
                ),
                A(
                    H2("Get Started Now!", cls="text-2xl"),
                    href="/signin",
                ),
                cls="text-center",
            )
        ],
    )
