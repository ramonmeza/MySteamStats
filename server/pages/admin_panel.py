from fasthtml.common import *

from ..components.app_input import AppSearchInput
from ..components.app_page import AppPage


def AdminPanel(session):
    return AppPage(
        Div(
            AppSearchInput(
                placeholder="Filter feedback...",
                no_results_message=P("No feedback found"),
            ),
            Div(id="feedbackList"),
            Div(
                I(cls="fa-solid fa-spinner text-primary animate-spin h-8 w-8"),
                id=f"loadingIcon",
                hx_trigger="load",
                hx_get="/admin/feedback",
                hx_target="#feedbackList",
                cls="htmx-indicator mx-auto w-max",
            ),
            cls="container mx-auto",
        ),
        Script(src="/public/js/components/appList.js"),
        session=session,
        title="Admin Panel",
    )
