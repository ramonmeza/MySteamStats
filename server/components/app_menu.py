from fasthtml.common import A, Div, Button, Li, Nav, P, Span, Title, Ul
from fasthtml.svg import Svg, Path

from typing import Any


def AppMenu(
    pages: list[tuple[str, str]], logo: Any = None, copyright: str | None = None
):
    """Creates an app menu

    Args:
        logo (Any): SVG for the logo
        pages (list[tuple[str, str]]): List of tuples with page name and their respective route: [('Home', '/'), ('About Us', '/about')]

    Returns:
        _type_: _description_
    """
    return Nav(
        A(Div(logo, cls="h-10"), cls="text-3xl font-bold leading-none", href="/"),
        Div(
            Button(
                Svg(
                    Title("Mobile menu"),
                    Path(d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"),
                    cls="block h-4 w-4 fill-current",
                    viewbox="0 0 20 20",
                    xmlns="http://www.w3.org/2000/svg",
                ),
                cls="navbar-burger flex items-center text-blue-600 p-3",
            ),
            cls="lg:hidden",
        ),
        Ul(
            *[
                Li(
                    # @todo: figure out current page highlighting
                    A(
                        page[0],
                        href=page[1],
                        cls="text-sm text-gray-400 hover:text-gray-500",
                    ),
                )
                for page in pages
            ],
            cls="hidden absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2 lg:flex lg:mx-auto lg:flex lg:items-center lg:w-auto lg:space-x-6"
        ),
        Div(
            Div(cls="navbar-backdrop fixed inset-0 bg-gray-800 opacity-25"),
            Nav(
                Div(
                    A(
                        Div(logo, cls="h-12"),
                        href="/",
                        cls="mr-auto text-3xl font-bold leading-none",
                    ),
                    Button(
                        Svg(
                            Path(
                                stroke_linecap="round",
                                stroke_linejoin="round",
                                stroke_width="2",
                                d="M6 18L18 6M6 6l12 12",
                            ),
                            xmlns="http://www.w3.org/2000/svg",
                            fill="none",
                            viewBox="0 0 24 24",
                            stroke="currentColor",
                            cls="h-6 w-6 text-gray-400 cursor-pointer hover:text-gray-500",
                        ),
                        cls="navbar-close",
                    ),
                    cls="flex items-center mb-8",
                ),
                Div(
                    Ul(
                        # @todo: figure out current page highlighting
                        *[
                            Li(
                                A(
                                    page[0],
                                    href=page[1],
                                    cls="block p-4 text-sm font-semibold text-gray-400 hover:bg-blue-50 hover:text-blue-600 rounded",
                                ),
                                cls="mb-1",
                            )
                            for page in pages
                        ]
                    )
                ),
                Div(
                    P(Span(copyright), cls="my-4 text-xs text-center text-gray-400"),
                    cls="mt-auto",
                ),
                cls="fixed top-0 left-0 bottom-0 flex flex-col w-5/6 max-w-sm py-6 px-6 bg-white border-r overflow-y-auto",
            ),
            cls="navbar-menu relative z-50 hidden",
        ),
        cls="relative px-4 py-4 flex justify-between items-center bg-white",
    )
