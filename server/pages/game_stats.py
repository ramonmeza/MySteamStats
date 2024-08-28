from fasthtml.common import *

from ..components.app_input import AppSearchInput

# from ..components.app_lists import
from ..components.app_page import AppPage
from ..components.app_lists import GameStatsList
from ..steamapi import SteamAPI


def GameStats(session, steam_api_key: str, appid: int):
    steamid: int = int(session.get("player")["steamid"])
    details: dict = SteamAPI.get_app_details(appid)[str(appid)]["data"]
    stats: dict = SteamAPI.ISteamUserStats.GetUserStatsForGame(
        steam_api_key, steamid, appid
    )
    schema: dict = SteamAPI.ISteamUserStats.GetSchemaForGame(steam_api_key, appid)

    if not stats or "stats" not in stats["playerstats"]:
        return AppPage(
            Div(
                H2(
                    details["name"],
                    cls="text-4xl font-black mb-8",
                ),
                P(
                    "You do not own this game, so no information is displayed."
                    if not stats
                    else "This game does not have trackable statistics."
                ),
                cls="container mx-auto text-center",
            ),
            Script(src="/public/js/components/filterList.js"),
            background=details["background"],
            session=session,
        )
    else:
        return AppPage(
            Div(
                H2(
                    details["name"],
                    cls="text-4xl font-black text-center text-semibold drop-shadow-md",
                ),
                AppSearchInput("Search for a stat...", P("No stats found")),
                GameStatsList(stats, schema),
                cls="container mx-auto",
            ),
            Script(src="/public/js/components/filterList.js"),
            background=details["background"],
            session=session,
        )
