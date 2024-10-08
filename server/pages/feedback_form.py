from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_input import AppInput, AppTextArea
from ..components.app_page import AppPage
from ..db import store_feedback


async def FeedbackSubmitted(form):
    try:
        id = await store_feedback(form["reason"], form["description"])
        return Div(
            P("Thanks for submitting your feedback!"),
            P(f"Feedback ID: {id}", cls="italic text-sm"),
            A(AppButton("Go Home"), href="/"),
        )
    except Exception as e:
        return Div(
            P(
                "An error occurred and your feedback may not have submitted.",
                cls="text-error italic font-semibold",
            ),
            A(AppButton("Go Home"), href="/"),
        )


def FeedbackForm(session, reason: str = ""):
    return AppPage(
        Div(
            H2(
                "Feedback Form",
                cls="mb-8 text-4xl font-black text-center",
            ),
            Form(
                AppInput(
                    value=reason,
                    name="reason",
                    readonly=bool(reason),
                    required=True,
                    maxlength=255,
                ),
                AppTextArea(
                    placeholder="Provide your feedback as clearly and concisely as possible to ensure our timely response.",
                    required=True,
                    name="description",
                    maxlength=1000,
                ),
                AppButton(
                    "Submit",
                    type="submit",
                    onclick="this.parentElement.checkValidity() ? this.classList.add('hidden') : this.classList.remove('hidden');",
                ),
                hx_post="/feedback",
                hx_target="#feedbackForm",
                hx_indicator="#loadingIcon",
                id="feedbackForm",
            ),
            Div(
                I(cls="fa-solid fa-spinner text-primary animate-spin h-8 w-8"),
                id="loadingIcon",
                cls="htmx-indicator",
            ),
            cls="container mx-auto text-center",
        ),
        session=session,
        title="Feedback Form",
    )
