from fasthtml.common import *


def AppLink(text: str, **kwargs):
    return A(
        text,
        **kwargs,
        cls="text-primary hover:text-primary-hover active:text-primary-active duration-300",
    )
