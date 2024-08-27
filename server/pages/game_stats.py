from fasthtml.common import *

from ..components.app_input import AppSearchInput

# from ..components.app_lists import
from ..components.app_page import AppPage
from ..components.app_lists import GameStatsList
from ..steamapi import SteamAPI


def GameStats(steam_api_key: str, steam_id: int, app_id: int):
    details: dict = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]
    stats: dict = SteamAPI.ISteamUserStats.GetUserStatsForGame(
        steam_api_key, steam_id, app_id
    )
    schema: dict = SteamAPI.ISteamUserStats.GetSchemaForGame(steam_api_key, app_id)

    if not stats:
        return AppPage(
            Div(
                H2(
                    details["name"],
                    cls="text-4xl font-black mb-8",
                ),
                P("You do not own this game, so no information is displayed."),
                cls="container mx-auto px-4 text-center",
            ),
            Script(src="/public/js/components/filterList.js"),
            background=details["background"],
            steamid=steam_id,
        )
    else:
        return AppPage(
            Div(
                H2(
                    details["name"],
                    cls="text-4xl font-black text-center",
                ),
                AppSearchInput("Search for a stat...", P("No stats found")),
                GameStatsList(stats, schema),
                cls="container mx-auto px-4",
            ),
            Script(src="/public/js/components/filterList.js"),
            background=details["background"],
            steamid=steam_id,
        )
