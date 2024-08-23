from fasthtml.common import Body, Div, H1, P, Title


def ErrorPage(request, exception):
    return (
        Title(f"GameStats: {exception}"),
        Body(
            Div(
                H1(exception.detail),
                P(f"Error code: {exception.status_code}"),
                P(repr(exception)),
            )
        ),
    )


exception_handlers = {
    500: lambda req, exc: (ErrorPage(req, exc)),
    404: lambda req, exc: ErrorPage(req, exc),
}
