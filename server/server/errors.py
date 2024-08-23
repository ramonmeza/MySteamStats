from fasthtml.common import Body, Button, Div, H1, P, Title

from .components.error_icon import ErrorIcon


def ErrorPage(request, exception):
    return (
        Title(f"GameStats: {str(exception)}"),
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
                Button(
                    "Go Back",
                    onclick="document.location = '/'",
                    cls="my-8 w-max px-4 py-2 rounded text-button-font bg-button hover:bg-button-hover animate-pulse hover:animate-none duration-200",
                ),
                cls="container mx-auto text-center",
            )
        ),
    )


exception_handlers = {
    500: lambda req, exc: ErrorPage(req, exc),
    404: lambda req, exc: ErrorPage(req, exc),
}
