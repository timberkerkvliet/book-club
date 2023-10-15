from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.get_invoker import get_invoker
from acceptance_tests.actions.invoke_api import FailedCommand
from book_club.app import App
from book_club.app_context import AppContext
from book_club.current_read.declare_new_read import DeclareNewRead
from book_club.request_handler import request_handler
from book_club.failure import Failure
from pyplay.action import Action, Expectation
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class AttemptHasFailed(Expectation):
    pass


@executes(AttemptHasFailed)
async def declare_read(
    log_book: LogBook,
    actor: Actor
):
    log_book.find().by_actor(actor.character_name).by_type(FailedCommand).one()

