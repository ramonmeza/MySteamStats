from fasthtml.common import Button
import typing


def AppButton(
    content: typing.Any,
    href: str | None = None,
    pulse: bool = False,
    shadow: bool = True,
    onclick: str | None = None,
    extracls: str | None = None,
    overridecls: bool = False,
):
    """onclick parameter takes precendence over href

    Args:
        content (typing.Any): HTML elements.
        href (str | None, optional): Link to navigate to when pressed.
        pulse (bool, optional): Whether to pulse. Defaults to False
        shadow (bool, optional): Display a shadow. Defaults to True.
        onclick (str | None, optional): onclick functionality. This will override `href` property.
        extracls (str | None, optional): Additional cls properties to apply. Will be appended to default styles unless `overridecls` is set to True.
        overridecls (bool, optional): Whether to override default cls styling with given extracls parameter. Defaults to False.

    Returns:
        _type_: _description_
    """
    appliedcls = "w-max px-4 py-2 mx-4 my-2 rounded text-app-text bg-app-accent hover:bg-app-accent-hover duration-300"
    if pulse:
        appliedcls += " animate-pulse hover:animate-none"

    if shadow:
        appliedcls += " shadow-lg hover:shadow-xl"

    if extracls:
        if overridecls:
            appliedcls = extracls
        else:
            appliedcls += f" {extracls}"

    # onclick parameter takes precendence over href
    applied_onclick = (
        onclick if onclick else f"document.location = '{href}';" if href else None
    )

    return Button(
        content,
        onclick=applied_onclick,
        cls=appliedcls,
    )
