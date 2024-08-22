from fasthtml.common import *

from ..components.game_card import GameCard
from ..supported_games import SUPPORTED_GAMES


def Home():
    return (
        Title("GameStats: Your Games, Your Stats"),
        Body(
            # main logo & tagline
            Div(
                H1("GameStats", cls="text-6xl font-bold"),
                P("Your Games, Your Stats", cls="text-lg italic"),
                Button(
                    "Get Started",
                    onclick="document.location = '/signin'",
                    cls="mt-4 py-2 px-4 animate-pulse hover:animate-none w-max mx-auto rounded text-white bg-blue-600 hover:bg-blue-300",
                ),
                # scroll icon
                Div(
                    Img(
                        src="/static/img/down_arrow.svg",
                        alt="Scroll for more",
                        cls="animate-bounce w-6 h-6 mx-auto",
                    ),
                    cls="absolute bottom-6 left-0 right-0",
                ),
                cls="min-w-screen min-h-screen flex flex-col justify-center text-center bg-gradient-to-b from-gray-100 to-gray-800",
            ),
            # features
            Div(
                Div(
                    H2("Stats Dashboard"),
                    P("Quickly access your library of games via Steam"),
                ),
                Div(
                    H2("Game Stats"),
                    P("Access hundreds of easily searchable statstical data points"),
                ),
                cls="min-w-screen min-h-screen bg-gray-800",
            ),
            # supported games list
            Div(
                H2("Supported Games", cls="text-3xl"),
                P("Below you'll find a complete list of officially supported games."),
                P(
                    "We are constantly adding new games and are willing to take your game ",
                    A("requests!", href="/request", cls="underline"),
                ),
                Div(
                    *[
                        GameCard(app_id, game_name)
                        for app_id, game_name in SUPPORTED_GAMES.items()
                    ],
                    cls="flex flex-wrap gap-4 justify-center p-4",
                ),
                cls="min-w-screen bg-gray-400 text-center",
            ),
            # footer
            Div(
                P(
                    "We'd love to hear your",
                    A("feedback!", href="/feedback", cls="underline"),
                ),
                P("Copyright © 2024 GameStats. All rights reserved."),
                cls="min-w-screen min-h-full text-center bg-gray-800 my-10 text-white",
            ),
            cls="min-w-screen min-h-screen bg-gray-800 cursor-default",
        ),
    )
