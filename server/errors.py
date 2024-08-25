from fasthtml.common import Body, Button, Div, H1, P, Title

from .components.app_button import AppButton
from .components.error_icon import ErrorIcon
from .strings import *


def ErrorPage(request, exception):
    return (
        Title(f"{SITE_NAME}: {str(exception)}"),
        Body(
            Div(
                ErrorIcon(cls="h-56 w-56 mx-auto"),
                H1(str(exception), cls="text-3xl"),
                (
                    P(f"Error code: {exception.status_code}", cls="italic text-sm")
                    if getattr(exception, "status_code", None)
                    else None
                ),
                P(repr(exception)),
                AppButton(
                    "Go Back",
                    href="/",
                ),
                cls="container mx-auto text-center",
            )
        ),
    )


exception_handlers = {
    500: lambda req, exc: ErrorPage(req, exc),
    404: lambda req, exc: ErrorPage(req, exc),
}
