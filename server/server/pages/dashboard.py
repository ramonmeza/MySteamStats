import fasthtml.common as fh


def Dashboard():
    return fh.Div(
        fh.A("Sign Out", href="/signout"), 
        fh.H1("Dashboard")
    )
