from fasthtml.common import Div, Script
from fasthtml.svg import Path, Svg


def AppScrollArrow():
    return Div(
        Svg(
            Path(
                d="M903.232 256l56.768 50.432L512 768 64 306.432 120.768 256 512 659.072z",
            ),
            viewBox="0 0 1024 1024",
            version="1.1",
            xmlns="http://www.w3.org/2000/svg",
            cls="animate-bounce w-6 h-6 mx-auto fill-app-accent dark:fill-app-dark-accent",
            onclick="clickScrollArrow();",
        ),
        Script(src="/public/js/components/scrollArrow.js"),
        id="AppScrollArrow",
        cls="fixed bottom-6 left-0 right-0 cursor-pointer duration-300",
    )
