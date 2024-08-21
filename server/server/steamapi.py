import requests

from typing import Literal

###
#
# API details here
#
# https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/
# use key:
# https://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=
#
###


class SteamAPI:

    @staticmethod
    def get_app_name(appid: int) -> str:
        app_list = SteamAPI.ISteamApps.GetAppList()
        return next(
            (x["name"] for x in app_list["applist"]["apps"] if x["appid"] == appid),
            "undefined",
        )

    @staticmethod
    def get_appid(app_name: str) -> int:
        app_list = SteamAPI.ISteamApps.GetAppList()
        return next(
            (x["appid"] for x in app_list["applist"]["apps"] if x["name"] == app_name),
            "",
        )

    @staticmethod
    def call(
        api: str,
        endpoint: str,
        api_version: int,
        format: Literal["json", "xml", "vdf"] = "json",
        **kwargs,
    ) -> dict | str | bytes:
        # remove params that have None value
        params = {k: v for k, v in kwargs.items() if v is not None}
        params["format"] = format

        # send request
        resp = requests.get(
            f"http://api.steampowered.com/{api}/{endpoint}/v{api_version:04}/",
            params=kwargs,
        )

        # return based on desired format
        if format == "json":
            return resp.json()
        elif format == "xml":
            return resp.text
        elif format == "vdf":
            return resp.content

    class ISteamApps:
        @staticmethod
        def GetAppList(api_version: Literal[1, 2] = 2):
            return SteamAPI.call(
                api="ISteamApps",
                endpoint="GetAppList",
                api_version=api_version,
            )

    class ISteamNews:
        @staticmethod
        def GetNewsForApp(
            api_version: Literal[1, 2],
            appid: int,
            maxlength: int | None = None,
            enddate: int | None = None,
            count: int | None = 20,
            feed: list[str] | None = None,
            tags: list[str] | None = None,
        ):
            """_summary_

            Args:
                api_version (Literal[1, 2]): _description_
                appid (int): AppID to retrieve news for
                maxlength (int, optional):Maximum length for the c…rb is generated to fit. Defaults to None.
                enddate (int, optional): Retrieve posts earlier t… (unix epoch timestamp). Defaults to None.
                count (int, optional): # of posts to retrieve. Defaults to 20.
                feed (list[str], optional): List of names to return news for. Defaults to None.
                tags (list[str], optional): List of tags. Defaults to None.

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamNews",
                endpoint="GetNewsForApp",
                api_version=api_version,
                appid=appid,
                maxlength=maxlength,
                enddate=enddate,
                count=count,
                feed=",".join(feed) if feed is not None else None,
                tags=",".join(tags) if tags is not None else None,
            )

    class ISteamUser:
        @staticmethod
        def GetFriendList(
            key: str, steamid: int, relationship: Literal["friend", "all"] = "friend"
        ):
            """_summary_

            Args:
                key (str): access key
                steamid (int): SteamID of user
                relationship (Literal["friend", "all"], optional): relationship type. Defaults to "friend".

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUser",
                endpoint="GetFriendList",
                api_version=1,
                key=key,
                steamid=steamid,
                relationship=relationship,
            )

        @staticmethod
        def GetPlayerBans(key: str, steamids: list[int]):
            """_summary_

            Args:
                key (str): access key
                steamids (list[int]): list of SteamIDs

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUser",
                endpoint="GetPlayerBans",
                api_version=1,
                key=key,
                steamids=",".join([str(x) for x in steamids]),
            )

        @staticmethod
        def GetPlayerSummaries(
            key: str, steamids: list[int], api_version: Literal[1, 2] = 2
        ):
            """_summary_

            Args:
                key (str): access key
                steamids (list[int]): list of SteamIDs (max: 100)
                api_version (Literal[1, 2], optional): API Version. Defaults to 2.

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUser",
                endpoint="GetPlayerSummaries",
                api_version=api_version,
                key=key,
                steamids=",".join([str(x) for x in steamids]),
            )

    class ISteamUserStats:
        @staticmethod
        def GetGlobalAchievementPercentagesForApp(
            gameid: int, api_version: Literal[1, 2] = 2
        ):
            """_summary_

            Args:
                gameid (int): GameID to retrieve the achievement percentages for
                api_version (Literal[1, 2], optional): API Version. Defaults to 2.

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUserStats",
                endpoint="GetGlobalAchievementPercentagesForApp",
                api_version=api_version,
                gameid=gameid,
            )

        @staticmethod
        def GetGlobalStatsForGame(
            appid: int,
            count: int,
            name: str,
            startdate: str | None = None,
            enddate: str | None = None,
        ):
            raise NotImplementedError

        @staticmethod
        def GetNumberOfCurrentPlayers(appid: int):
            """_summary_

            Args:
                appid (int): AppID that we're getting user count for

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUserStats",
                endpoint="GetNumberOfCurrentPlayers",
                api_version=1,
                appid=appid,
            )

        @staticmethod
        def GetPlayerAchievements(
            key: str, steamid: int, appid: int, l: str = "english"
        ):
            """_summary_

            Args:
                key (str): access key
                steamid (int): SteamID of user
                appid (int): AppID to get achievements for
                l (str, optional): Language to return strings for. Defaults to "english".

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUserStats",
                endpoint="GetPlayerAchievements",
                api_version=1,
                key=key,
                steamid=steamid,
                appid=appid,
                l=l,
            )

        @staticmethod
        def GetSchemaForGame(
            key: str, appid: int, l: str = "english", api_version: Literal[1, 2] = 2
        ):
            """_summary_

            Args:
                key (str): _description_
                appid (int): _description_
                l (str, optional): _description_. Defaults to "english".
                api_version (Literal[1, 2], optional): _description_. Defaults to 2.

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUserStats",
                endpoint="GetSchemaForGame",
                api_version=api_version,
                key=key,
                appid=appid,
                l=l,
            )

        @staticmethod
        def GetUserStatsForGame(
            key: str, steamid: int, appid: int, api_version: Literal[1, 2] = 2
        ):
            """_summary_

            Args:
                key (str): access key
                steamid (int): SteamID of user
                appid (int): appid of game
                api_version (Litera[1, 2], optional): API Version. Defaults to 2.

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="ISteamUserStats",
                endpoint="GetUserStatsForGame",
                api_version=api_version,
                key=key,
                steamid=steamid,
                appid=appid,
            )

    class IPlayerService:
        @staticmethod
        def GetRecentlyPlayedGames(key: str, steamid: int, count: int = 0):
            """_summary_

            Args:
                key (str): Access key
                steamid (int): The player we're asking about
                count (int, optional): The number of games to return (0/unset: all). Defaults to 0.

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="IPlayerService",
                endpoint="GetRecentlyPlayedGames",
                api_version=1,
                key=key,
                steamid=steamid,
                count=count,
            )

        @staticmethod
        def GetOwnedGames(
            key: str,
            steamid: int,
            appids_filter: list[int] = [],
            include_free_sub: bool = False,
            include_extended_appinfo: bool = False,
            include_app_info: bool = False,
            include_played_free_games: bool = False,
            skip_unvetted_apps: bool = False,
            language: str = "english",
        ):
            """_summary_

            Args:
                key (str): Access key
                steamid (int): The player we're asking about
                appids_filter (list[int], optional): if set, restricts result set to the passed in apps
                include_free_sub (bool): Some games are in the free sub, which are excluded by default.
                include_extended_appinfo (bool): true if we want even mor…info must also be true.. Defaults to False.
                include_app_info (bool): true if we want additional details (name, icon) about each game. Defaults to False.
                include_played_free_games (bool): Free games are excluded by default.  If this is set, free games the user has played will be returned. Defaults to False.
                skip_unvetted_apps (bool, optional): if set, skip unvetted store apps. Defaults to False.
                language (str): Will return appinfo in this language. Defaults to "english".

            Returns:
                _type_: _description_
            """
            appid_filter_params = {
                f"appids_filter[{i}]": v for i, v in enumerate(appids_filter)
            }
            return SteamAPI.call(
                api="IPlayerService",
                endpoint="GetOwnedGames",
                api_version=1,
                key=key,
                steamid=steamid,
                **appid_filter_params,
                include_free_sub=include_free_sub,
                include_extended_appinfo=include_extended_appinfo,
                include_app_info=include_app_info,
                include_played_free_games=include_played_free_games,
                skip_unvetted_apps=skip_unvetted_apps,
                language=language,
            )

        @staticmethod
        def GetSteamLevel(key: str, steamid: int):
            """_summary_

            Args:
                key (str): Access key
                steamid (int): The player we're asking about

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="IPlayerService",
                endpoint="GetSteamLevel",
                api_version=1,
                key=key,
                steamid=steamid,
            )

        @staticmethod
        def GetBadges(key: str, steamid: int):
            """_summary_

            Args:
                key (str): Access key
                steamid (int): The player we're asking about

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="IPlayerService",
                endpoint="GetBadges",
                api_version=1,
                key=key,
                steamid=steamid,
            )

        @staticmethod
        def GetCommunityBadgeProgress(key: str, steamid: int, badgeid: int):
            """_summary_

            Args:
                key (str): Access key
                steamid (int): The player we're asking about
                badgeid (int): The badge we're asking about

            Returns:
                _type_: _description_
            """
            return SteamAPI.call(
                api="IPlayerService",
                endpoint="GetCommunityBadgeProgress",
                api_version=1,
                key=key,
                steamid=steamid,
                badgeid=badgeid,
            )
