from fasthtml.common import *
from fasthtml.svg import Circle, G, Path, Svg


def AppList(
    *items,
    searchable: bool = False,
    placeholder: str = "Search...",
    no_results_found_message: str = "No results found."
):
    return Div(
        (
            Input(
                placeholder=placeholder,
                onkeyup="filterAppList(this.value, this.nextElementSibling.children);",
                cls="min-w-full bg-app-input-background text-app-input-text my-4 px-2 py-1 border-2 border-transparent focus:outline-none focus:ring-2 focus:ring-app-accent",
            )
            if searchable
            else None
        ),
        Div(
            *items,
            cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-center items-center gap-2"
        ),
        Div(
            P(
                no_results_found_message,
                cls="text-sm text-center",
            ),
            Svg(
                G(
                    Path(
                        d="M147.998,0C66.392,0,0,66.392,0,147.998c0,81.606,66.392,147.998,147.998,147.998c81.606,0,147.998-66.392,147.998-147.998 C295.996,66.392,229.604,0,147.998,0z M147.998,279.996c-36.257,0-69.143-14.696-93.023-38.44 c-9.536-9.482-17.631-20.41-23.934-32.42C21.442,190.847,16,170.047,16,147.998C16,75.214,75.214,16,147.998,16 c34.523,0,65.987,13.328,89.533,35.102c12.208,11.288,22.289,24.844,29.558,39.996c8.27,17.239,12.907,36.538,12.907,56.9 C279.996,220.782,220.782,279.996,147.998,279.996z"
                    ),
                    Path(
                        d="M163.638,187.607c17.554,3.671,33.322,13.54,44.4,27.789l12.631-9.82c-13.402-17.24-32.494-29.184-53.756-33.631 c-34.195-7.146-70.146,6.052-91.587,33.631l12.633,9.82C105.675,192.607,135.382,181.697,163.638,187.607z"
                    ),
                    Circle(cx="98.666", cy="114.998", r="16"),
                    Circle(cx="197.666", cy="114.998", r="16"),
                ),
                viewBox="0 0 295.996 295.996",
                xmlns="http://www.w3.org/2000/svg",
                cls="fill-app-accent h-24 w-24 mx-auto m-4",
            ),
            id="NoResultsFound",
            cls="hidden",
        ),
    )
