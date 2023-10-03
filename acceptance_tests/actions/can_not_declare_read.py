from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.get_invoker import get_invoker
from book_club.app import App
from book_club.app_context import AppContext
from book_club.current_read.declare_new_read import DeclareNewRead
from book_club.request_handler import request_handler
from book_club.failure import Failure
from pyplay.action import Action, Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class CanNotDeclareRead(Assertion):
    book_name: str


@executes(CanNotDeclareRead)
async def declare_read(
    action: CanNotDeclareRead,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app = await stage_props(App)
    handler = request_handler(app.context)

    result = await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=DeclareNewRead(
            book_name=action.book_name
        )
    )

    assert result == Failure()
