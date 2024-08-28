from fasthtml.common import Div
from fasthtml.svg import G, Rect, Svg, Text, Tspan
from typing import Literal


def AppLogo(
    cls=None, auto_switch: bool = False, fill: str = "fill-dark dark:fill-light"
):

    icon_cls = "w-full h-full block md:hidden" if auto_switch else "hidden"
    logo_cls = "w-full h-full hidden md:block" if auto_switch else "w-full h-full"

    return Div(
        Svg(
            G(
                Text(
                    Tspan(
                        "MySteam",
                        x="160.64",
                        y="259.691",
                        style="font-size: 50.3px; word-spacing: 0px;",
                    ),
                    Tspan(
                        "Stats",
                        x="344",
                        y="259.691",
                        cls="fill-primary",
                        style="font-weight: 600; font-size: 50.3px; word-spacing: 0px;",
                    ),
                    cls=fill,
                    style="font-family: Coolvetica; font-size: 51px; white-space: pre; opacity: 1; transform-origin: -0.199419px -2.54803px;",
                    y="-0.63",
                    transform="matrix(0.994781, 0, 0, 0.992557, 0.199419, 2.548036)",
                ),
                Rect(
                    x="121.987",
                    y="240.328",
                    width="10",
                    height="19.864",
                    cls="fill-primary-hover",
                ),
                Rect(
                    x="133.87",
                    y="227.384",
                    width="10",
                    height="33",
                    cls="fill-primary",
                ),
                Rect(
                    x="145.827",
                    y="233.425",
                    width="10",
                    height="26.959",
                    cls="fill-primary-hover",
                ),
                # transform="matrix(1, 0, 0, 1, -23.73033332824707, 0.15976101160049438)",
            ),
            viewBox="121.987 207.522 338 65",
            xmlns="http://www.w3.org/2000/svg",
            cls=logo_cls,
        ),
        Svg(
            G(
                Rect(
                    x="121.987",
                    y="240.517",
                    width="10",
                    height="19.864",
                    cls="fill-primary-hover",
                ),
                Rect(
                    x="133.87",
                    y="227.384",
                    width="10",
                    height="33",
                    cls="fill-primary",
                ),
                Rect(
                    x="145.827",
                    y="233.425",
                    width="10",
                    height="26.959",
                    cls="fill-primary-hover",
                ),
                transform="matrix(1, 0, 0, 1, -47.76963424682617, -20.056758880615234)",
            ),
            viewBox="74.2174 207.3272 33.84 33",
            xmlns="http://www.w3.org/2000/svg",
            cls=icon_cls,
        ),
        cls=cls,
    )


# <?xml version="1.0" encoding="utf-8"?>
# <svg viewBox="101.041 207.522 378.95 59.096" xmlns="http://www.w3.org/2000/svg">
#   <g transform="matrix(1, 0, 0, 1, -10.600333213806152, -7.84023904800415)">
#     <text style="fill: rgb(51, 51, 51); font-family: Coolvetica; font-size: 51px; white-space: pre; opacity: 1; transform-origin: -0.199419px -2.54803px;" y="-0.63" transform="matrix(0.994781, 0, 0, 0.992557, 0.199419, 2.548036)"><tspan x="160.64" y="259.691" style="fill: rgb(21, 21, 21); font-size: 50.3px; word-spacing: 0px;">MySteam</tspan><tspan style="fill: rgb(179, 23, 214); font-weight: 900; font-size: 50.3px; word-spacing: 0px;">Stats</tspan></text>
#     <rect x="121.987" y="240.328" width="10" height="19.864" style="stroke: rgb(0, 0, 0); paint-order: fill; fill-rule: nonzero; stroke-opacity: 0; opacity: 1; fill: rgb(232, 185, 243);"/>
#     <rect x="133.87" y="227.384" width="10" height="33" style="stroke: rgb(0, 0, 0); paint-order: fill; fill-rule: nonzero; stroke-opacity: 0; opacity: 1; fill: rgb(179, 23, 214);"/>
#     <rect x="145.827" y="233.425" width="10" height="26.959" style="stroke: rgb(0, 0, 0); paint-order: fill; fill-rule: nonzero; stroke-opacity: 0; opacity: 1; fill: rgb(232, 185, 243);"/>
#   </g>
# </svg>

# return Svg(
#     G(
#         Text(
#             Tspan(
#                 "MySteam",
#                 x="160.64",
#                 y="259.691",
#                 cls="fill-dark dark:fill-light",
#                 style="font-size: 50.3px; word-spacing: 0px;",
#             ),
#             Tspan(
#                 "Stats",
#                 cls="fill-primary",
#                 style="font-weight: 900; font-size: 50.3px; word-spacing: 0px;",
#             ),
#             style="font-family: Coolvetica; font-size: 51px; white-space: pre; opacity: 1; transform-origin: -0.199419px -2.54803px;",
#             y="-0.63",
#             transform="matrix(0.994781, 0, 0, 0.992557, 0.199419, 2.548036)",
#         ),
#         Rect(
#             x="121.987",
#             y="240.328",
#             width="10",
#             height="19.864",
#             cls="fill-primary-hover",
#             style="stroke: rgb(0, 0, 0); paint-order: fill; fill-rule: nonzero; stroke-opacity: 0; opacity: 1;;",
#         ),
#         Rect(
#             x="133.87",
#             y="227.384",
#             width="10",
#             height="33",
#             cls="fill-primary",
#             style="stroke: rgb(0, 0, 0); paint-order: fill; fill-rule: nonzero; stroke-opacity: 0; opacity: 1;",
#         ),
#         Rect(
#             x="145.827",
#             y="233.425",
#             width="10",
#             height="26.959",
#             cls="fill-primary-hover",
#             style="stroke: rgb(0, 0, 0); paint-order: fill; fill-rule: nonzero; stroke-opacity: 0; opacity: 1;",
#         ),
#         transform="matrix(1, 0, 0, 1, -10.600333213806152, -7.84023904800415)",
#     ),
#     viewBox="101.041 207.522 378.95 59.096",
#     xmlns="http://www.w3.org/2000/svg",
#     cls="h-6",
# )
