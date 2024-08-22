from fasthtml.common import *


def Layout(title: str = "", children: list = []):
    return (
        Title(f"GameStats {title}" if title else "GameStats: Your Games, Your Stats"),
        Div(
            Main(
                Div(
                    *children,
                    cls="container mx-auto",
                )
            ),
            cls="bg-gray-100",
        ),
        Footer(
            Div(
                "Copyright © 2024 GameStats. All rights reserved.",
                cls="p-10 min-w-full text-center text-gray-100",
            ),
        ),
    )
