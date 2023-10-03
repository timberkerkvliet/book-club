from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from book_club.app_context import AppContext
from book_club.member_list.kick_member import KickMember as KickMemberCommand
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class KickMember(Action):
    character_name: str


@executes(KickMember)
async def let_character_leave_club(
    action: KickMember,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)

    await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=KickMemberCommand(name=action.character_name, )
    )
