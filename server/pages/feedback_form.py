from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_input import AppInput, AppTextArea
from ..components.app_page import AppPage
from ..db import store_feedback


def FeedbackSubmitted(form):
    try:
        id = store_feedback(form["reason"], form["description"])
        return Div(
            P("Thanks for submitting your feedback!"),
            P(f"Feedback ID: {id}", cls="italic text-sm"),
            A(AppButton("Go Home"), href="/"),
        )
    except Exception as e:
        return Div(
            P(
                "An error occurred and your feedback may not have submitted.",
                cls="text-red-500 italic font-semibold",
            ),
            A(AppButton("Go Home"), href="/"),
        )


def FeedbackForm(reason: str = "", steamid=None):
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
                onsubmit="""validateForm(event);""",
                id="feedbackForm",
            ),
            Div(
                I(cls="fa-solid fa-spinner text-primary animate-spin h-8 w-8"),
                id="loadingIcon",
                cls="htmx-indicator",
            ),
            cls="container mx-auto px-4 text-center",
        ),
        Script(
            code="""
function validateForm(event) {
    # event.target.reason.value = sanitize(event.target.reason.value);
    # event.target.description.value = sanitize(event.target.description.value);
}
               """
        ),
        steamid=steamid,
    )
