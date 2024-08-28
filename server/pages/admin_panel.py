from fasthtml.common import *

from ..components.app_input import AppSearchInput
from ..components.app_lists import FeedbackList
from ..components.app_page import AppPage
from ..db import get_all_feedback


def AdminPanel(session):
    return AppPage(
        Div(
            AppSearchInput(
                placeholder="Filter feedback...",
                no_results_message=P("No stats found"),
            ),
            FeedbackList(get_all_feedback()),
            cls="container mx-auto",
        ),
        Script(src="/public/js/components/filterList.js"),
        session=session,
        title="Admin Panel",
    )
