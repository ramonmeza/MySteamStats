import fasthtml.common as fh


exception_handlers = {
    500: lambda req, exc: fh.Titled(
        "500",
        fh.Div(fh.H1("Uh oh..."), fh.P("We screwed up")),
    ),
    404: lambda req, exc: fh.Titled(
        "404 Not Found",
        fh.Div(fh.H1("Uh oh..."), fh.P("We can't find what you're looking for.")),
    ),
}
