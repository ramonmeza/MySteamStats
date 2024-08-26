from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_hamburger_menu import AppHamburgerMenu
from ..components.app_layout import AppLayout
from ..components.app_page import AppPage
from ..strings import APP_NAME


def FeedbackForm(reason: str):
    return AppLayout(
        AppPage(
            AppHamburgerMenu(AppButton("Home", href="/")),
            Div(
                H1(
                    APP_NAME,
                    cls="font-black text-4xl p-4 text-center",
                ),
                Div(
                    H2("Feedback Form", cls="text-2xl font-bold text-app-accent"),
                    H2("Reason", cls="text-lg font-semibold"),
                    Select(
                        *[
                            Option(r, selected=True if reason == r else False)
                            for r in ["App Feedback", "Game Request"]
                        ],
                        cls="bg-app-input-background text-app-input-text px-2 py-1 border-2 border-transparent focus:outline-none focus:ring-2 focus:ring-app-accent",
                    ),
                    H2("Message", cls="text-lg font-semibold"),
                    Textarea(
                        placeholder="Write your message here...",
                        cls="bg-app-input-background text-app-input-text px-2 py-1 border-2 border-transparent focus:outline-none focus:ring-2 focus:ring-app-accent",
                    ),
                    AppButton("Submit"),
                    cls="grid grid-cols-1 text-center place-items-stretch gap-4",
                ),
                cls="container mx-auto",
            ),
        ),
        Script(src="/public/js/components/appList.js"),
        Script(src="/public/js/components/appHamburgerMenu.js"),
        title=f"{APP_NAME}: {reason}",
    )
