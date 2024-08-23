from fasthtml.common import *

from ..supported_games import SUPPORTED_GAMES


def GameStats(app_id: int):
    game_name: str = SUPPORTED_GAMES[app_id]
    return (
        Title(f"GameStats: {game_name}"),
        Body(
            Div(H1(game_name), P("Show stats")),
        ),
    )
