from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.get_invoker import get_invoker
from book_club.app import App
from book_club.app_context import AppContext
from book_club.member_list.add_member import AddMember
from book_club.member_list.kick_member import KickMember
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook, LogMessage
from pyplay.prop import Props


@dataclass
class CanNotKickMember(Action):
    character_name: str


@executes(CanNotKickMember)
async def let_character_leave_club(
    action: CanNotKickMember,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app = await stage_props(App)
    handler = request_handler(app.context)

    await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=KickMember(name=action.character_name, )
    )
