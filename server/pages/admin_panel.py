from fasthtml.common import *

from ..components.app_page import AppPage
from ..db import get_feedback


def AdminPanel(session):
    return AppPage(session=session, title="Admin Panel")
