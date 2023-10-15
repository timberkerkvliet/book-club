from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.invoke_api import FailedCommand
from pyplay.action import Expectation
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook


@dataclass
class CommandHasFailed(Expectation):
    pass


@executes(CommandHasFailed)
async def declare_read(
    log_book: LogBook,
    actor: Actor
):
    log_book.find().by_actor(actor.character_name).by_type(FailedCommand).one()

