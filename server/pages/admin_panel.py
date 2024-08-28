from fasthtml.common import *

from ..components.app_page import AppPage
from ..db import get_feedback


def AdminPanel(player=None):
    return AppPage(player=player, title="Admin Panel")
