from fasthtml.common import *


def AppLink(content, href: str):
    return A(
        content,
        href=href,
        cls="text-app-accent hover:text-app-accent-hover underline duration-300",
    )
