from fasthtml.common import *


def AppImage(src: str, alt: str = "", href: str | None = None, **kwargs):
    appliedcls = "shadow-lg"

    if href:
        appliedcls += " hover:shadow-xl border-2 rounded border-transparent hover:border-app-accent duration-300"

    return Div(
        Img(
            src=src,
            alt=alt,
            onclick=f"document.location = '{href}';" if href else None,
        ),
        cls=appliedcls,
        **kwargs,
    )
