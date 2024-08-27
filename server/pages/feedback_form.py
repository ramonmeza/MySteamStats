from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_input import AppInput, AppTextArea
from ..components.app_page import AppPage


def FeedbackSubmitted():
    return Div(
        P("Thanks for submitting your feedback!"), A(AppButton("Go Home"), href="/")
    )


def FeedbackForm(reason: str = "", steamid=None):
    return AppPage(
        Div(
            H2(
                "Feedback Form",
                cls="mb-8 text-4xl text-app-accent dark:text-app-dark-accent font-black text-center",
            ),
            P(
                "Please note: the form is not yet functional.",
                cls="text-red-500 italic font-semibold",
            ),
            Form(
                AppInput(reason, readonly=bool(reason)),
                AppTextArea(
                    "Provide your feedback as clearly and concisely as possible to ensure our timely response."
                ),
                AppButton("Submit", type="submit"),
                hx_post="/feedback",
                hx_target="#feedbackForm",
                id="feedbackForm",
            ),
            cls="container mx-auto px-4 text-center",
        ),
        steamid=steamid,
    )
