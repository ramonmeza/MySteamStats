import json

from fasthtml.common import *

from ..steamapi import SteamAPI
from ..supported_games import SUPPORTED_GAMES


def GameStats(steam_api_key: str, steam_id: int, app_id: int):
    details = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]
    stats = SteamAPI.ISteamUserStats.GetUserStatsForGame(
        steam_api_key, steam_id, app_id
    )
    game_name: str = details["name"]

    return (
        Title(f"GameStats: {game_name}"),
        Body(
            Div(
                Div(
                    H1(game_name, cls="text-3xl"),
                    Button(
                        "Dashboard",
                        onclick="document.location = '/dashboard'",
                        cls="w-max ml-auto px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover duration-300",
                    ),
                    Button(
                        "Sign Out",
                        onclick="document.location = '/signout'",
                        cls="w-max ml-auto px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover duration-300",
                    ),
                    cls="flex flex-cols py-8",
                ),
                Div(
                    P(json.dumps(details, indent=4)),
                    P(" --- "),
                    P(" --- "),
                    P(" --- "),
                    P(json.dumps(stats, indent=4)),
                ),
                Div(
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
                            cls="text-textcolor3 text-sm",
                        ),
                        cls="mt-auto",
                    ),
                    cls="py-12 flex flex-col text-center grow",
                ),
                cls="px-4 flex flex-col min-h-screen",
            ),
            cls="container mx-auto",
        ),
    )
