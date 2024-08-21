import fasthtml.common as fh


def set_toast(session, type, message):
    session["toast-type"] = type
    session["toast-message"] = message


def handle_toasts(session):
    # show toast messages if needed
    toast_type: str = session.get("toast-type", None)
    if toast_type is not None:
        toast_message: str = session.get("toast-message")
        fh.add_toast(session, toast_message, toast_type)

        # reset toast in session object
        set_toast(session, None, None)
