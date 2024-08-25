from fasthtml.common import *  # A, Body, Div, H1, Table, Td, Th, Title, Tr

from ..steamapi import SteamAPI
from ..supported_games import SUPPORTED_GAMES


def DashboardCard(game: dict):
    app_id = game["appid"]
    details: dict = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]

    return Div(
        Img(src=details["header_image"], cls="h-16 rounded-l-lg"),
        Div(details["name"], cls="pl-4 text-lg my-auto"),
        Div(
            f"{game['playtime_forever'] / 60:.1f} hrs",
            cls="text-xs my-auto ml-auto mr-4 text-textcolor2",
        ),
        onclick=f"document.location = '/stats/{app_id}'",
        cls="flex flex-row bg-color1 hover:bg-color2 rounded-lg cursor-pointer shadow hover:shadow-lg transition-shadow",
    )


def Dashboard(steam_api_key: str, steam_id: int):
    data: dict = SteamAPI.IPlayerService.GetOwnedGames(
        key=steam_api_key, steamid=steam_id, appids_filter=SUPPORTED_GAMES.keys()
    )["response"]

    return (
        Title("GameStats: Dashboard"),
        Body(
            Div(
                Div(
                    H1("Dashboard", cls="text-3xl"),
                    Button(
                        "Sign Out",
                        onclick="document.location = '/signout'",
                        cls="w-max ml-auto px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover duration-300",
                    ),
                    cls="grid grid-cols-2 py-8",
                ),
                Div(
                    *[DashboardCard(game) for game in data["games"]],
                    cls="grid grid-rows-1 gap-4",
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
        ),
    )
