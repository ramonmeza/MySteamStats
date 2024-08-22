import fasthtml.common as fh

from .layout import Layout
from ..steamapi import SteamAPI
from ..supported_games import SUPPORTED_GAMES


def Dashboard(steam_api_key: str, steam_id: int):
    data: dict = SteamAPI.IPlayerService.GetOwnedGames(
        key=steam_api_key, steamid=steam_id, appids_filter=SUPPORTED_GAMES.keys()
    )

    game_table = fh.Table(
        fh.Tr(
            fh.Th("Game Name"),
            fh.Th("App ID"),
            fh.Th("Playtime (last 2 weeks)"),
            fh.Th("Total Playtime"),
        ),
        *[
            fh.Tr(
                fh.Td(SUPPORTED_GAMES[game["appid"]]),
                fh.Td(game["appid"]),
                fh.Td(f'{game["playtime_2weeks"] / 60:.2f}hrs'),
                fh.Td(f'{game["playtime_forever"] / 60:.2f}hrs'),
                onclick="document.location = '/stats/" + str(game["appid"]) + "'",
                cls="hover:bg-blue-300 hover:cursor-pointer",
            )
            for game in data["response"]["games"]
        ],
    )

    return Layout(
        "Dashboard",
        fh.Div(fh.A("Sign Out", href="/signout"), fh.H1("Dashboard"), game_table),
    )
