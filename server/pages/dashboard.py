from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_hamburger_menu import AppHamburgerMenu
from ..components.app_image import AppImage
from ..components.app_layout import AppLayout
from ..components.app_link import AppLink
from ..components.app_list import AppList
from ..components.app_page import AppPage

from ..steamapi import SteamAPI
from ..strings import *
from ..supported_games import SUPPORTED_GAMES


def GameListItem(app_id: int, **kwargs):
    details: dict = SteamAPI.get_app_details(app_id)[str(app_id)]
    if not bool(details["success"]):
        print(f"Failed to get details for owned game with appid {app_id}")
        # @todo error-handling, maybe an error toast would be nice
        return None

    details = details["data"]

    return AppImage(
        src=details["header_image"],
        alt=details["name"],
        href=f"/stats/{app_id}",
        data_searchterms=[int(app_id), details["name"]],
    )


def Dashboard(steam_api_key: str, steam_id: int):
    owned_games: dict = SteamAPI.IPlayerService.GetOwnedGames(
        key=steam_api_key, steamid=steam_id, appids_filter=SUPPORTED_GAMES.keys()
    )["response"]

    return AppLayout(
        AppPage(
            AppHamburgerMenu(AppButton("Sign Out", href="/signout")),
            H2(
                "Game ",
                Span("Dashboard", cls="text-app-accent"),
                cls="text-4xl font-black shadow-lg text-center",
            ),
            AppList(
                *[GameListItem(int(game["appid"])) for game in owned_games["games"]],
                searchable=True,
                placeholder="Search for a game...",
                no_results_found_message=Span(
                    "Game not supported. Make a ",
                    AppLink(
                        "request",
                        href="/feedback?reason=Request Game",
                    ),
                    " to support this game!",
                ),
            ),
            Div(
                P(
                    "We'd love to hear your ",
                    AppLink(
                        "feedback",
                        href="/feedback?reason=App Feedback",
                    ),
                    "!",
                    cls="text-sm text-center",
                ),
                cls="w-full p-8",
            ),
        ),
        Script(src="/public/js/components/appList.js"),
        Script(src="/public/js/components/appHamburgerMenu.js"),
    )
