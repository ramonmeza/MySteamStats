from fasthtml.common import Div, H1, P
from fasthtml.svg import Path, Svg

from .components.app_button import AppButton
from .components.app_layout import AppLayout
from .components.app_page import AppPage
from .strings import APP_NAME


def ErrorIcon():
    return Div(
        Svg(
            Path(
                fillrule="evenodd",
                clip_rule="evenodd",
                d="M38.155 140.475L48.988 62.1108L92.869 67.0568L111.437 91.0118L103.396 148.121L38.155 140.475ZM84.013 94.0018L88.827 71.8068L54.046 68.3068L44.192 135.457L98.335 142.084L104.877 96.8088L84.013 94.0018ZM59.771 123.595C59.394 123.099 56.05 120.299 55.421 119.433C64.32 109.522 86.05 109.645 92.085 122.757C91.08 123.128 86.59 125.072 85.71 125.567C83.192 118.25 68.445 115.942 59.771 123.595ZM76.503 96.4988L72.837 99.2588L67.322 92.6168L59.815 96.6468L56.786 91.5778L63.615 88.1508L59.089 82.6988L64.589 79.0188L68.979 85.4578L76.798 81.5328L79.154 86.2638L72.107 90.0468L76.503 96.4988Z",
                fill="#ffffff",
            ),
            viewBox="-20 0 190 190",
            version="1.1",
            xmlns="http://www.w3.org/2000/svg",
            fill="none",
        ),
        cls="h-56 w-56 mx-auto",
    )


def ErrorPage(request, exception):
    return AppLayout(
        AppPage(
            ErrorIcon(),
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
        ),
        title=f"{APP_NAME}: {str(exception)}",
    )


exception_handlers = {
    500: lambda req, exc: ErrorPage(req, exc),
    404: lambda req, exc: ErrorPage(req, exc),
}
