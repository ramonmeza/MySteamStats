import fasthtml.common as fh


def Landing():
    return fh.Div(
        fh.H1("Hello, World!"),
        fh.P("Hi"),
        (
            fh.A(
                "Sign In",
                href="/signin",
            )
        ),
    )
