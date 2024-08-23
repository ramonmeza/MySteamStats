from fasthtml.common import A, Body, Div, H1, Table, Td, Th, Title, Tr

from ..steamapi import SteamAPI
from ..supported_games import SUPPORTED_GAMES


def Dashboard(steam_api_key: str, steam_id: int):
    data: dict = SteamAPI.IPlayerService.GetOwnedGames(
        key=steam_api_key, steamid=steam_id, appids_filter=SUPPORTED_GAMES.keys()
    )

    game_table: Table = Table(
        Tr(
            Th("Game Name"),
            Th("Total Playtime"),
        ),
        *[
            Tr(
                Td(SUPPORTED_GAMES[game["appid"]]),
                Td(f'{game["playtime_forever"] / 60:.2f}hrs'),
                onclick="document.location = '/stats/" + str(game["appid"]) + "'",
                cls="hover:bg-blue-300 hover:cursor-pointer",
            )
            for game in data["response"]["games"]
        ],
    )

    return (
        Title("GameStats Dashboard"),
        Body(
            Div(
                A("Sign Out", href="/signout"),
                H1("Dashboard"),
                game_table,
                cls="container mx-auto",
            ),
            cls="min-w-screen min-h-screen",
        ),
    )
