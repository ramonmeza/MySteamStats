import fasthtml.common as fh

from ..steamapi import SteamAPI
from ..strings import *


SUPPORTED_GAMES = {
    730: "Counter-Strike 2"
}


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
                fh.Td(f"{game["playtime_2weeks"] / 60:.2f}hrs"),
                fh.Td(f"{game["playtime_forever"] / 60:.2f}hrs"),
            )
            for game in data["response"]["games"]
        ],
    )

    return fh.Div(fh.A(SIGNOUT, href="/signout"), fh.H1(DASHBOARD), game_table)
