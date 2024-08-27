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


def GameStatsListItem(stat_name: str, stat_value, fallback_name: str = "Unknown Stat"):
    if not stat_name:
        stat_name = fallback_name

    return Div(
        H3(
            stat_name,
            cls="text-lg font-semibold text-app-accent dark:text-app-dark-accent",
        ),
        P(stat_value, cls="italic"),
        data_searchterms=stat_name,
        cls="overflow-scroll bg-app-bg dark:bg-app-dark-bg hover:bg-app-bg-hover dark:hover:bg-app-dark-bg-hover px-4 py-2",
    )


def GameStatsList(stats: dict, schema: dict):
    return (
        Div(
            *[
                GameStatsListItem(
                    next(
                        iter(
                            [
                                x
                                for x in schema["game"]["availableGameStats"]["stats"]
                                if x["name"] == stat["name"]
                            ]
                        )
                    )["displayName"],
                    stat["value"],
                    fallback_name=stat["name"],
                )
                for stat in stats["playerstats"]["stats"]
            ],
            cls="grid justify-items-stretch grid-cols-1 md:grid-cols-2 lg:grid-cols-3 place-items-center gap-2",
        ),
    )
