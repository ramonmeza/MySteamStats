from fasthtml.common import *

from ..components.app_input import AppSearchInput
from ..components.app_link import AppLink
from ..components.app_lists import GameList
from ..components.app_page import AppPage
from ..steamapi import SteamAPI
from ..supported_games import SUPPORTED_GAMES


def Dashboard(steam_api_key: str, steam_id: int):
    owned_games: dict = SteamAPI.IPlayerService.GetOwnedGames(
        key=steam_api_key,
        steamid=steam_id,
        include_free_sub=True,
        appids_filter=[game["appid"] for game in SUPPORTED_GAMES],
    )["response"]["games"]

    return AppPage(
        Div(
            H2(
                "Dashboard",
                cls="mb-8 text-4xl text-app-accent dark:text-app-dark-accent font-black text-center",
            ),
            AppSearchInput(
                "Search for a game...",
                no_results_message=P(
                    "No games found! Feel free to ",
                    AppLink(
                        "request a game",
                        href="/feedback?reason=Game Request",
                    ),
                    "!",
                    cls="text-sm text-center",
                ),
            ),
            GameList(owned_games),
            cls="container mx-auto px-4",
        ),
        Script(src="/public/js/components/filterList.js"),
        steamid=steam_id,
    )
