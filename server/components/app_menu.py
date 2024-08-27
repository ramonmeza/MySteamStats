from fasthtml.common import *


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
                cls="text-lg font-semibold mx-2",
            ),
        )
        if player
        else I(Title("Menu"), cls="fa-solid fa-bars")
    )

    return Div(
        Div(
            Div(
                A(menu_icon, onclick="toggleMenu();"),
                cls="grow-0",
            ),
            Div(
                H1("MySteamStats", cls="text-xl"),
                cls="grow text-center",
            ),
            Div(
                Button(
                    I(cls="fa-regular fa-moon", id="AppDarkModeToggle"),
                    onclick="toggleDarkMode();",
                    cls="h-8 w-8",
                ),
                cls="grow-0",
            ),
            Script(src="/public/js/components/appMenu.js"),
            cls="flex flex-row items-stretch p-4 h-full",
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
        cls=f"fixed z-50 top-0 left-0 h-16 w-full bg-primary shadow {'hidden' if hidden else ''}",
    )
