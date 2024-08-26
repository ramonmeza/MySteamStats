from fasthtml.common import *


def AppButton(*content, type: str = "button"):
    return (
        Button(
            *content,
            type=type,
            cls="w-max px-4 py-2 mx-4 my-2 rounded text-app-text bg-app-accent hover:bg-app-accent-hover duration-300 animate-pulse hover:animate-none",
        ),
    )
