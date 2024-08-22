from fasthtml.common import *

from ..steamapi import SteamAPI


def GameCard(app_id: int, game_name: str):
    game_details = SteamAPI.get_app_details(app_id)[str(app_id)]["data"]
    return Div(
        Img(
            src=game_details["header_image"],
            alt=game_name,
            cls="rounded-lg shadow-md hover:shadow-xl transition-shadow",
        ),
    )
