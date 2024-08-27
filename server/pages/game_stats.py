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

    return AppPage(
        Div(
            H2(
                details["name"],
                cls="text-4xl text-app-accent dark:text-app-dark-accent font-black text-center",
            ),
            # @todo: add search input and search list for stats
            AppSearchInput("Search for a stat...", P("No stats found")),
            GameStatsList(stats, schema),
            cls="container mx-auto px-4",
        ),
        Script(src="/public/js/components/filterList.js"),
        background=details["background"],
        steamid=steam_id,
    )


# AppLayout(
#             AppHamburgerMenu(
#                 AppButton('Dashboard', href="/dashboard"),
#                 AppButton("Sign Out", href="/signout")),
#             AppPage(
#                 H2(
#                     Span("Your Stats", cls="text-app-accent"),
#                     cls="text-4xl font-black shadow-lg text-center",
#                 ),
#                 H2(
#                     details["name"],
#                     cls="text-4xl font-black shadow-lg text-center",
#                 ),
#                 AppList(
#                     *[
#                         GameStatListItem(stat, next(x for x in schema['game']['availableGameStats']['stats'] if x['name'] == stat['name']))
#                         for stat in stats["playerstats"]["stats"]
#                     ],
#                     searchable=True,
#                     placeholder="Search for a stat...",
#                     no_results_found_message="No stats found."
#                 ),
#                 Details(
#                     Summary("Raw JSON Data"),
#                     Div(
#                         Pre(Code(json.dumps(stats, indent=4), cls="language-json"))
#                     ),
#                     open="",
#                 )
#             ),
#             Script(src="/public/js/components/appList.js"),
#             Script(src="/public/js/components/appHamburgerMenu.js"),
#             Link(rel="stylesheet", href="/public/css/highlight.min.css"),
#             Script(src="/public/js/highlight.min.js"),
#             Script(src="/public/js/highlight-json.min.js"),
#             Script(code="""hljs.highlightAll();"""),
#             title=f"{APP_NAME}: {details["name"]}",
#         )
