from fasthtml.common import *


def GameStats(app_id: int, game_name: str):
    return (
        Title(f"GameStats: {game_name}"),
        Body(Div(H1(game_name), P("Show stats")), cls="min-w-screen min-h-screen"),
    )
