from fasthtml.common import A, Button, Div, H1, I, Li, Script, Title, Ul

from ..components.app_link import AppLink


def AppMenu(steamid: int):
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
                AppLink(H1("MySteamStats", cls="text-xl"), href="/"),
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
            Script(
                code="""
                function toggleMenu() {
                   const linkMenu = document.getElementById("AppLinks");
                   linkMenu.classList.toggle("hidden");
                }
                
                function loadDarkModeIcon() {
                    const toggleIconElem = document.getElementById("AppDarkModeToggle");
                    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                        document.documentElement.classList.add('dark');
                        
                        toggleIconElem.classList.add("fa-regular");
                        toggleIconElem.classList.add("fa-moon");

                        toggleIconElem.classList.remove("fa-solid");
                        toggleIconElem.classList.remove("fa-sun");
                    } else {
                        document.documentElement.classList.remove('dark');

                        toggleIconElem.classList.remove("fa-regular");
                        toggleIconElem.classList.remove("fa-moon");
                        
                        toggleIconElem.classList.add("fa-solid");
                        toggleIconElem.classList.add("fa-sun");
                    }
                }

                addEventListener("load", loadDarkModeIcon);

                function toggleDarkMode() {
                   const toggleIconElem = document.getElementById("AppDarkModeToggle");

                    document.documentElement.classList.toggle('dark');
                   
                   if (document.documentElement.classList.contains("dark")) {
                        localStorage.theme = 'dark';
                        toggleIconElem.classList.add("fa-regular");
                        toggleIconElem.classList.add("fa-moon");

                        toggleIconElem.classList.remove("fa-solid");
                        toggleIconElem.classList.remove("fa-sun");
                   } else {
                        localStorage.theme = 'light';
                        toggleIconElem.classList.remove("fa-regular");
                        toggleIconElem.classList.remove("fa-moon");
                        
                        toggleIconElem.classList.add("fa-solid");
                        toggleIconElem.classList.add("fa-sun");
                   }

                   toggleIconElem.classList.toggle("fa-regular");
                   toggleIconElem.classList.toggle("fa-moon");
                   toggleIconElem.classList.toggle("fa-solid");
                   toggleIconElem.classList.toggle("fa-sun");
                   
                }
            """
            ),
            cls="flex flex-row items-center p-4",
        ),
        Div(
            Ul(
                *[
                    A(
                        Li(
                            link[0],
                            cls="uppercase p-4 hover:bg-app-bg-hover dark:hover:bg-app-dark-bg-hover",
                        ),
                        href=link[1],
                    )
                    for link in endpoints
                ]
            ),
            id="AppLinks",
            cls="hidden w-full text-center bg-app-bg dark:bg-app-dark-bg",
        ),
        id="AppMenu",
        cls="fixed z-50 top-0 left-0 h-16 w-full bg-app-bg dark:bg-app-dark-bg shadow",
    )
