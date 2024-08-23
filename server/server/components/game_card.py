from fasthtml.common import *

from ..steamapi import SteamAPI


def GameCard(app_id: int, game_name: str):
    game_details = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]
    return (
        Img(
            src=game_details["header_image"],
            alt=game_name,
            cls="rounded-lg border-4 border-transparent duration-300 hover:border-color1",
        ),
    )
