from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.invoke_api import invoke_api
from book_club.app import App
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
    return await invoke_api(
        command=DeclareNewRead(
            book_name=action.book_name
        ),
        app=await stage_props(App),
        log_book=log_book,
        character_name=actor.character_name,
    )
