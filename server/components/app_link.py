from fasthtml.common import *


def AppLink(text: str, href: str):
    return A(
        text,
        href=href,
        cls="text-app-accent dark:text-app-dark-accent hover:text-app-accent-hover dark:hover:text-app-dark-accent-hover",
    )
