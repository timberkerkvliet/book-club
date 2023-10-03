from asyncio import create_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from acceptance_tests import actions
from book_club.app import App
from pyplay.action_executor import find_executors_in_module
from pyplay.logger import pyplay_logger
from pyplay.play_execution import pyplay_spec


@asynccontextmanager
async def fake_app() -> AsyncGenerator[App, None]:
    app = App(fake_adapters=True)
    create_task(app.run())
    yield app

book_club_spec = pyplay_spec(
    narrator=pyplay_logger(),
    prop_factories={
        App: fake_app
    },
    action_executors=find_executors_in_module(actions)
)
