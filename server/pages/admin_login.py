from fasthtml.common import *

from ..components.app_button import AppButton
from ..components.app_input import AppInput
from ..components.app_page import AppPage


def AdminLogin(player=None):
    return AppPage(
        Div(
            H2(
                "Admin Login",
                cls="mb-8 text-4xl font-black text-center",
            ),
            Form(
                AppInput(
                    placeholder="Email",
                    name="email",
                    type="email",
                    required=True,
                ),
                AppInput(
                    placeholder="Password",
                    name="password",
                    type="password",
                    required=True,
                ),
                AppButton(
                    "Submit",
                    type="submit",
                    onclick="this.parentElement.checkValidity() ? this.classList.add('hidden') : this.classList.remove('hidden');",
                ),
                hx_post="/auth/admin",
                hx_target="#loginForm",
                hx_indicator="#loadingIcon",
                id="loginForm",
            ),
            Div(
                I(cls="fa-solid fa-spinner text-primary animate-spin h-8 w-8"),
                id="loadingIcon",
                cls="htmx-indicator",
            ),
            cls="container mx-auto text-center",
        ),
        player=player,
        title="Admin Login",
    )
