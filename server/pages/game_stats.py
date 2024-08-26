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
            AppHamburgerMenu(
                AppButton('Dashboard', href="/dashboard"),
                AppButton("Sign Out", href="/signout")),
            AppPage(
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
            AppPage(
                H2("Raw JSON Data"),
                Pre(Code(json.dumps(stats, indent=4), cls="language-json"))
            ),
            Script(src="/public/js/components/appList.js"),
            Script(src="/public/js/components/appHamburgerMenu.js"),
            title=f"{APP_NAME}: {details["name"]}",
        )

    # return (
    #     Title(f"{SITE_NAME}: {game_name}"),
    #     Body(
    #         Link(rel="stylesheet", href="/public/css/highlight.min.css"),
    #         Script(src="/public/js/highlight.min.js"),
    #         Script(src="/public/js/highlight-json.min.js"),
    #         Div(
    #             Div(
    #                 H1(game_name, cls="text-3xl"),
    #                 Div(
    #                     AppButton(
    #                         "Dashboard",
    #                         href="/dashboard",
    #                     ),
    #                     AppButton(
    #                         "Sign Out",
    #                         href="/signout",
    #                     ),
    #                     cls="ml-auto",
    #                 ),
    #                 cls="flex flex-cols py-8",
    #             ),
    #             Div(
    #                 Input(id="FilterInput", type="text", onkeyup="filterList()", placeholder="Search for a stat...", cls="text-black rounded shadow-md p-2"),
    #                 Ul(
    #                     *[
    #                         Li(f"{next(y['displayName'] if y['displayName'] else y['name'] for y in stats_schema['game']['availableGameStats']['stats'] if y['name'] == x['name'])} = {x["value"]}")
    #                         for x in stats["playerstats"]["stats"]
    #                     ],
    #                     id="StatsList",
    #                 ),
    #                 Pre(Code(json.dumps(stats, indent=4), cls="language-json")),
    #                 cls="container mx-auto",
    #             ),
    #             SiteFooter(),
    #             cls="px-4 flex flex-col min-h-screen",
    #         ),
    #         Script(code="hljs.highlightAll();"),
    #         Script(src="/public/js/filterList.js"),
    #         cls="container mx-auto",
    #     ),
    # )
