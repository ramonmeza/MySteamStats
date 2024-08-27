from fasthtml.common import add_toast
from typing import Literal


# this may look crazy, but i needed to wrap toast functions
# to account for redirects within the app itself.
# if i create a toast then redirected, the toast didnt popup,
# so i store it in the session and check on it when after a reroute
def set_toast(
    session,
    type: Literal[
        "info",
        "success",
        "warning",
        "error",
    ],
    message: str,
):
    session["toast-type"] = type
    session["toast-message"] = message


def handle_toasts(session):
    # show toast messages if needed
    toast_type: str = session.get("toast-type", None)
    if toast_type is not None:
        toast_message: str = session.get("toast-message")
        add_toast(session, toast_message, toast_type)

        # reset toast in session object
        set_toast(session, None, None)
