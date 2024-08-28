from fasthtml.common import *

from ..steamapi import SteamAPI
from ..components.app_input import AppTextArea


def GridList(*items):
    return (
        Div(
            items,
            cls="grid content-center gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-4",
        ),
    )


def GameList(games: list[dict]):
    return (
        GridList(
            *[GameListItem(data["appid"]) for data in games],
        ),
    )


def GameStatsList(stats: dict, schema: dict):
    return GridList(
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
    )


def FeedbackList(records):
    return GridList(
        *[
            FeedbackListItem(record["id"], record["reason"], record["description"])
            for record in records
        ],
    )


def GameListItem(appid: int):
    details: dict = SteamAPI.get_app_details(appid)[str(appid)]

    if not bool(details["success"]):
        err = f"Failed to get details for owned game with appid {appid}"
        print(err)
        return Script(code=f'console.warn("{err}");')

    details = details["data"]

    return (
        A(
            Img(src=details["header_image"]),
            href=f"/stats/{appid}",
            cls="shadow dark:shadow-none hover:shadow-lg transition-shadow mx-auto inner-border-2 border-transparent hover:border-primary active:border-primary-active",
            data_searchterms=",".join([str(appid), details["name"]]),
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
        cls="overflow-scroll bg-mid text-light px-4 py-2 text-center shadow dark:shadow-none hover:shadow-lg transition-shadow",
    )


def FeedbackListItem(id, reason, description):
    return Div(
        Div(
            # @todo: make button functional
            H1(reason, cls="py-2 text-base text-primary font-light"),
            Button(I(cls="fa fa-trash text-error"), cls="ml-auto"),
            cls="flex",
        ),
        P('"', description, '"', cls="pl-2 pb-2"),
        data_searchterms=[reason, description],
        cls="bg-mid hover:bg-mid-hover px-4 py-2 text-light shadow dark:shadow-none hover:shadow-lg transition-shadow",
    )
