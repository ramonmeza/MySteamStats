from fasthtml.common import *

from ..steamapi import SteamAPI


def GameListItem(appid: int):
    details: dict = SteamAPI.get_app_details(appid)[str(appid)]

    if not bool(details["success"]):
        err = f"Failed to get details for owned game with appid {appid}"
        print(err)
        return Script(code=f'console.warn("{err}");')

    details = details["data"]

    return A(
        Img(src=details["header_image"]),
        href=f"/stats/{appid}",
        cls="border-2 border-transparent hover:border-primary active:border-primary-active",
        data_searchterms=",".join([str(appid), details["name"]]),
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
            cls="text-base font-light",
        ),
        P(
            (f"{stat_value:,}" if str(stat_value).isdigit() else stat_value),
            cls="italic text-primary text-4xl font-black",
        ),
        data_searchterms=stat_name,
        # hover:bg-app-bg-hover dark:hover:bg-app-dark-bg-hover
        cls="overflow-scroll bg-light dark:bg-dark px-4 py-2 text-center",
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
