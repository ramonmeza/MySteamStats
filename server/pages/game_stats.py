import json

from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_hamburger_menu import AppHamburgerMenu
from ..components.app_list import AppList
from ..components.app_layout import AppLayout
from ..components.app_page import AppPage
from ..steamapi import SteamAPI
from ..strings import *
from ..supported_games import SUPPORTED_GAMES


def GameStatListItem(stat, schema):
    display_name: str = schema['displayName']
    return Div(
        H3(display_name if display_name else stat['name'], cls="text-lg font-semibold text-accent"),
        P(stat["value"], cls="italic"),
        data_searchterms=[schema, stat['name']],
        cls="bg-app-layer-background hover:bg-app-layer-background-hover shadow-lg hover:shadow-xl rounded py-2 px-4"
    )


def GameStats(steam_api_key: str, steam_id: int, app_id: int):
    details: dict = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]
    stats: dict = SteamAPI.ISteamUserStats.GetUserStatsForGame(
        steam_api_key, steam_id, app_id
    )
    schema: dict = SteamAPI.ISteamUserStats.GetSchemaForGame(
        steam_api_key, app_id
    )

    return AppLayout(
        AppPage(
            AppHamburgerMenu(
                AppButton("Dashboard", href="/dashboard"),
                AppButton("Sign Out", href="/signout")),
            H2(
                Span("Your Stats", cls="text-app-accent"),
                cls="text-4xl font-black shadow-lg text-center",
            ),
            H2(
                details["name"],
                cls="text-4xl font-black shadow-lg text-center",
            ),
            AppList(
                *[
                    GameStatListItem(stat, next(x for x in schema['game']['availableGameStats']['stats'] if x['name'] == stat['name']))
                    for stat in stats["playerstats"]["stats"]
                ],
                searchable=True,
                placeholder="Search for a stat...",
                no_results_found_message="No stats found."
            ),
        ),
        Script(src="/public/js/components/appList.js"),
        Script(src="/public/js/components/appHamburgerMenu.js"),
        title=f"{APP_NAME}: {details["name"]}",
    )
