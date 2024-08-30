from fasthtml.common import *


def AppTextArea(*content, **kwargs):
    return Textarea(
        *content,
        **kwargs,
        cls="h-64 w-full bg-light dark:bg-dark text-dark dark:text-light my-4 px-2 py-1 border border-dark-menu-item-active focus:outline-none focus:ring-2 focus:ring-primary dark:focus:ring-primary",
    )


def AppInput(*content, **kwargs):
    return (
        Input(
            *content,
            **kwargs,
            cls="w-full bg-light dark:bg-dark text-dark dark:text-light my-4 px-2 py-1 border border-dark-menu-item-active focus:outline-none focus:ring-2 focus:ring-primary dark:focus:ring-primary",
        ),
    )


def AppSearchInput(placeholder: str, no_results_message):
    return (
        Div(
            AppInput(
                placeholder=placeholder,
                onkeyup="filterList(this.value, document.getElementById('appList').children);",
            ),
            Div(
                I(cls="fa-solid fa-magnifying-glass h-32 w-32"),
                no_results_message,
                id="NoResultsFound",
                cls="hidden text-center",
            ),
        ),
    )
