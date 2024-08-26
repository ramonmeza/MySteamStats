from fasthtml.common import *


def AppTextArea(placeholder: str):
    return Textarea(
        placeholder=placeholder,
        cls="h-64 w-full bg-app-input dark:bg-app-dark-input text-app-input-text dark:text-app-dark-input-text my-4 px-2 py-1 border-2 border-transparent focus:outline-none focus:ring-2 focus:ring-app-accent dark:focus:ring-app-dark-accent",
    )


def AppInput(placeholder: str, onkeyup: str = None, readonly: bool = False):
    return (
        Input(
            placeholder=placeholder,
            onkeyup=onkeyup,
            readonly=readonly,
            cls="w-full bg-app-input dark:bg-app-dark-input text-app-input-text dark:text-app-dark-input-text my-4 px-2 py-1 border-2 border-transparent focus:outline-none focus:ring-2 focus:ring-app-accent dark:focus:ring-app-dark-accent",
        ),
    )


def AppSearchInput(placeholder: str, no_results_message):
    return (
        Div(
            AppInput(
                placeholder=placeholder,
                onkeyup="filterList(this.value, this.parentElement.nextElementSibling.children);",
            ),
            Div(
                I(
                    cls="fa-solid fa-magnifying-glass h-32 w-32 text-app-accent dark:text-app-dark-accent"
                ),
                no_results_message,
                id="NoResultsFound",
                cls="hidden text-center",
            ),
        ),
    )
