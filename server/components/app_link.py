from fasthtml.common import *


def AppLink(text: str, href: str):
    return A(
        text,
        href=href,
        cls="text-primary hover:text-primary-hover active:text-primary-active duration-300",
    )
