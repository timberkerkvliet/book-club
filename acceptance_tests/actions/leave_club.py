from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.get_invoker import get_invoker
from book_club.app_context import AppContext
from book_club.member_list.join_club import JoinClub
from book_club.member_list.kick_member import KickMember
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook, LogMessage
from pyplay.prop import Props


@dataclass
class LetCharacterLeaveClub(Action):
    character_name: str


@executes(LetCharacterLeaveClub)
async def let_character_leave_club(
    action: LetCharacterLeaveClub,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)

    await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=KickMember(name=action.character_name, )
    )