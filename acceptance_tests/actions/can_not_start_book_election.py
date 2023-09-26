from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from book_club.app_context import AppContext
from book_club.book_election.start_book_election import StartBookElection as StartBookElectionCommand
from book_club.app import request_handler
from book_club.failure import Failure
from pyplay.action import Action, Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class CanNotStartBookElection(Assertion):
    pass


@executes(CanNotStartBookElection)
async def add_actor_as_new_member(
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)

    result = await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=StartBookElectionCommand(book_names=[])
    )

    assert result == Failure()