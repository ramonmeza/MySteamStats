from fasthtml.common import *


def AppButton(*content, type: str = "button", **kwargs):
    return (
        Button(
            *content,
            type=type,
            **kwargs,
            cls="text-light bg-primary hover:bg-primary-hover active:bg-primary-active w-max px-4 py-2 mx-4 my-2 rounded duration-300 animate-pulse hover:animate-none",
        ),
    )
