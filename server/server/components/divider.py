from fasthtml.common import Div, Hr


def Divider(cls=None):
    return Div(
        Hr(
            cls="border-0 h-px bg-gradient-to-r from-transparent from-15% via-white to-85% to-transparent"
        ),
        cls=cls,
    )
