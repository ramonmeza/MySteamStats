import fasthtml.common as fh


def SignIn():
    return fh.Div(
        fh.H1("Sign In"),
        fh.A(
            fh.Img(
                src="/static/img/steam_signin_chonky.png",
                alt="Sign in through STEAM",
            ),
            href="/signin/steam/",
        ),
    )
