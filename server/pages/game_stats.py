import json

from fasthtml.common import *

from ..steamapi import SteamAPI
from ..supported_games import SUPPORTED_GAMES


def GameStats(steam_api_key: str, steam_id: int, app_id: int):
    details: dict = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]
    stats: dict = SteamAPI.ISteamUserStats.GetUserStatsForGame(
        steam_api_key, steam_id, app_id
    )
    stats_schema: dict = SteamAPI.ISteamUserStats.GetSchemaForGame(steam_api_key, app_id)
    game_name: str = details["name"]
    
    return (
        Title(f"GameStats: {game_name}"),
        Body(
            Link(rel="stylesheet", href="/public/css/highlight.min.css"),
            Script(src="/public/js/highlight.min.js"),
            Script(src="/public/js/highlight-json.min.js"),
            Div(
                Div(
                    H1(game_name, cls="text-3xl"),
                    Div(
                        Button(
                            "Dashboard",
                            onclick="document.location = '/dashboard'",
                            cls="w-max px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover duration-300",
                        ),
                        Button(
                            "Sign Out",
                            onclick="document.location = '/signout'",
                            cls="w-max px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover duration-300",
                        ),
                        cls="ml-auto",
                    ),
                    cls="flex flex-cols py-8",
                ),
                Div(
                    Input(id="FilterInput", type="text", onkeyup="filterList()", placeholder="Search for a stat...", cls="text-black rounded shadow-md p-2"),
                    Ul(
                        *[
                            Li(f"{next(y['displayName'] if y['displayName'] else y['name'] for y in stats_schema['game']['availableGameStats']['stats'] if y['name'] == x['name'])} = {x["value"]}")
                            for x in stats["playerstats"]["stats"]
                        ],
                        id="StatsList",
                    ),
                    Pre(Code(json.dumps(stats, indent=4), cls="language-json")),
                    cls="container mx-auto",
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
            Script(code="hljs.highlightAll();"),
            Script(src="/public/js/filterList.js"),
            cls="container mx-auto",
        ),
    )
