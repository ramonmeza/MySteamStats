from fasthtml.common import Button
import typing


def AppButton(
    content: typing.Any,
    href: str | None = None,
    pulse: bool = False,
    shadow: bool = True,
    extracls: str | None = None,
    overridecls: bool = False,
):
    cls = "w-max px-4 py-2 mx-4 my-2 rounded text-button-font bg-button hover:bg-button-hover duration-300"
    if pulse:
        cls += " animate-pulse hover:animate-none"

    if shadow:
        cls += " shadow hover:shadow-lg"

    if extracls:
        if overridecls:
            cls = extracls
        else:
            cls += f" {extracls}"

    return Button(
        content,
        onclick=f"document.location = '{href}';",
        cls=cls,
    )
