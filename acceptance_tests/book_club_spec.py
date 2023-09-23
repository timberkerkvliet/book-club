from contextlib import asynccontextmanager

from acceptance_tests import actions
from book_club.app import app
from book_club.app_context import AppContext
from pyplay.action_executor import find_executors_in_module
from pyplay.logger import pyplay_logger
from pyplay.play_execution import pyplay_spec


@asynccontextmanager
async def fake_app_context():
    async with app(is_fake=True) as app_context:
        yield app_context

book_club_spec = pyplay_spec(
    narrator=pyplay_logger(),
    prop_factories={
        AppContext: fake_app_context
    },
    action_executors=find_executors_in_module(actions)
)
