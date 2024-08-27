from fasthtml.common import A, Button, Div, H1, I, Li, Script, Title, Ul


def AppMenu(steamid: int, hidden: bool = False):
    endpoints = (
        [
            ("Dashboard", "/dashboard"),
            ("Request Game", "/feedback?reason=Request Game"),
            ("Report Issue", "/feedback?reason=Report Issue"),
            ("Sign Out", "/signout"),
        ]
        if steamid
        else [("Home", "/"), ("Sign In", "/signin/steam")]
    )

    return Div(
        Div(
            Div(
                Button(
                    I(Title("Menu"), cls="fa-solid fa-bars"),
                    onclick="toggleMenu();",
                    cls="h-6 w-6",
                ),
                cls="grow-0 self-start",
            ),
            Div(
                A(H1("MySteamStats", cls="text-xl"), href="/"),
                cls="grow text-center",
            ),
            Div(
                Button(
                    I(cls="fa-regular fa-moon", id="AppDarkModeToggle"),
                    onclick="toggleDarkMode();",
                    cls="h-6 w-6",
                ),
                cls="grow-0 self-end",
            ),
            Script(src="/public/js/components/appMenu.js"),
            cls="flex flex-row items-center p-4",
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
