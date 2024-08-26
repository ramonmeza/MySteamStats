from fasthtml.common import *


def AppPage(*components, cls=None):
    appliedcls = (
        "min-w-screen min-h-screen flex flex-col justify-center items-center p-4"
    )

    if cls:
        appliedcls += " "
        appliedcls += cls

    return Div(
        components,
        cls=appliedcls,
    )
