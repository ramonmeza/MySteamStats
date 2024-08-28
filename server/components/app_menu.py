from fasthtml.common import *

from .app_logo import AppLogo


def AppMenu(player: dict, hidden: bool = False):
    endpoints = (
        [
            ("Dashboard", "/dashboard"),
            ("Request Game", "/feedback?reason=Request Game"),
            ("Report Issue", "/feedback?reason=Report Issue"),
            ("Sign Out", "/signout"),
        ]
        if player
        else [("Home", "/"), ("Sign In", "/signin/steam")]
    )

    menu_icon = (
        Div(
            Img(
                src=player["avatarfull"],
                cls="w-8 my-auto inline rounded-full border-2 border-green-400",
            ),
            Span(
                player["personaname"],
                cls="text-lg font-semibold mx-2 hidden md:inline-block",
            ),
        )
        if player
        else I(Title("Menu"), cls="fa-solid fa-bars")
    )

    return Div(
        Div(
            Div(
                menu_icon,
                onclick="toggleMenu();",
                cls="cursor-pointer justify-self-start",
            ),
            AppLogo(cls="h-8 justify-self-center"),
            Div(
                Button(
                    I(cls="fa-regular fa-moon", id="AppDarkModeToggle"),
                    onclick="toggleDarkMode();",
                    cls="h-8 w-8 cursor-pointer",
                ),
                cls="justify-self-end",
            ),
            Script(src="/public/js/components/appMenu.js"),
            cls="grid grid-cols-3 items-center p-4 h-full",
        ),
        Div(
            Ul(
                *[
                    A(
                        Li(
                            link[0],
                            cls="uppercase p-4 hover:bg-menu-item-hover dark:hover:bg-dark-menu-item-hover active:bg-menu-item-active dark:active:bg-dark-menu-item-active",
                        ),
                        href=link[1],
                    )
                    for link in endpoints
                ]
            ),
            id="AppLinks",
            cls="hidden w-full text-center bg-menu-item dark:bg-dark-menu-item",
        ),
        id="AppMenu",
        cls=f"fixed z-50 top-0 left-0 h-16 w-full bg-mid shadow {'hidden' if hidden else ''}",
    )
