from fasthtml.common import Div
from fasthtml.svg import Path, Svg


def DownArrow(onclick: str | None = None, **kwargs):
    return Div(
        Svg(
            Path(
                d="M903.232 256l56.768 50.432L512 768 64 306.432 120.768 256 512 659.072z",
                fill="#9ca3af",
            ),
            viewBox="0 0 1024 1024",
            version="1.1",
            xmlns="http://www.w3.org/2000/svg",
            fill="#9ca3af",
            cls="animate-bounce w-6 h-6 mx-auto",
            onclick=onclick,
        ),
        **kwargs,
    )
