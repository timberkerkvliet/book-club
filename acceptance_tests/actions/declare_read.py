from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from book_club.app_context import AppContext
from book_club.current_read.declare_new_read import DeclareNewRead
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class DeclareRead(Action):
    book_name: str


@executes(DeclareRead)
async def declare_read(
    action: DeclareRead,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app = await stage_props(App)
    handler = request_handler(app.context)

    invoker_log = log_book.find().by_actor(actor.character_name).by_type(MyInvokerIs).one()

    await handler.handle_command(
        invoker=invoker_log.invoker,
        command=DeclareNewRead(
            book_name=action.book_name
        )
    )
