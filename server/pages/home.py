from fasthtml.common import Div, H1, H2, P, Span

from ..components.app_button import AppButton
from ..components.app_image import AppImage
from ..components.app_layout import AppLayout
from ..components.app_link import AppLink
from ..components.app_list import AppList
from ..components.app_page import AppPage

from ..steamapi import SteamAPI
from ..strings import APP_NAME
from ..supported_games import SUPPORTED_GAMES


def Home():
    return AppLayout(
        AppPage(
            H1(APP_NAME, cls="text-5xl font-black shadow-lg"),
            P(
                "Your Games, Your Stats",
                cls="text-sm italic shadow-lg text-app-accent",
            ),
            AppButton("Get Started", pulse=True, href="/signin/steam/"),
        ),
        AppPage(
            Div(
                H2(
                    "Game ",
                    Span("Dashboard", cls="text-app-accent"),
                    cls="text-3xl font-black shadow-lg text-center",
                ),
                P("Quickly access stats for any of your favorite Steam games!"),
            ),
            Div(
                H2(
                    "All of ",
                    Span("Your", cls="text-app-accent"),
                    "Stats",
                    cls="text-3xl font-black shadow-lg text-center",
                ),
                P(
                    "Each game is packed with statistics that reflect your time playing the game!"
                ),
            ),
            Div(
                H2(
                    Span("Expanding", cls="text-app-accent"),
                    " Support",
                    cls="text-3xl font-black shadow-lg text-center",
                ),
                P("Custom supported games showcase your stats in unique, themed ways!"),
            ),
            cls="gap-24",
        ),
        AppPage(
            Div(
                H2(
                    "Supported ",
                    Span("Games", cls="text-app-accent"),
                    cls="text-3xl font-black shadow-lg text-center mb-8",
                ),
                AppList(
                    *[
                        AppImage(
                            SteamAPI.get_app_details(app_id)[str(app_id)]["data"][
                                "header_image"
                            ],
                        )
                        for app_id in SUPPORTED_GAMES.keys()
                    ],
                ),
            ),
            Div(
                P(
                    "We'd love to hear your ",
                    AppLink(
                        "feedback",
                        href="/feedback?reason=App Feedback",
                    ),
                    "!",
                    cls="text-sm text-center",
                ),
                cls="w-full p-8",
            ),
        ),
        navigation_arrow=True,
    )
