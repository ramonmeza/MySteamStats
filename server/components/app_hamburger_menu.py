from fasthtml.common import *
from fasthtml.svg import Path, Svg


from .app_button import AppButton


def AppHamburgerMenu(*content):
    return Div(
        Div(
            AppButton(
                Svg(
                    Title("Mobile menu"),
                    Path(d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"),
                    cls="h-6 w-6 fill-app-accent hover:fill-app-accent-hover duration-300",
                    viewBox="0 0 20 20",
                    xmlns="http://www.w3.org/2000/svg",
                ),
                onclick="toggleHamburgerMenu();",
                extracls="navbar-burger flex items-center w-full p-4",
                overridecls=True,
            ),
            cls="inline-block my-auto",
        ),
        Div(*content, id="HamburgerMenu", cls="inline-block hidden"),
        cls="fixed top-0 left-0 h-max w-full flex flex-row bg-app-background",
    )
