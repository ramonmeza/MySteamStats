from fasthtml.common import *

from ..steamapi import SteamAPI


def GameListItem(app_id: int):
    details: dict = SteamAPI.get_app_details(app_id)[str(app_id)]

    if not bool(details["success"]):
        err = f"Failed to get details for owned game with appid {app_id}"
        print(err)
        return Script(code=f'console.warn("{err}");')

    details = details["data"]

    return A(
        Img(src=details["header_image"]),
        href=f"/stats/{app_id}",
        cls="border-2 border-transparent hover:border-app-accent dark:hover:border-app-dark-accent",
        data_searchterms=",".join([str(app_id), details["name"]]),
    )


def GameList(games: list[dict]):
    return (
        Div(
            *[GameListItem(data["appid"]) for data in games],
            cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 place-items-center gap-2",
        ),
    )
