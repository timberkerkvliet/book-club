from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from acceptance_tests.actions.member_joined import MemberJoined
from book_club.app import App
from book_club.app_context import AppContext
from book_club.failure import Failure
from book_club.member_list.add_member import AddMember as AddMemberCommand
from book_club.request_handler import request_handler
from pyplay.action import Action, Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class CanNotAddMember(Assertion):
    character_name: str


@executes(CanNotAddMember)
async def can_not_add_actor_as_new_member(
    action: CanNotAddMember,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app = await stage_props(App)
    handler = request_handler(app.context)

    result = await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=AddMemberCommand(
            name=action.character_name,
            mail_address=f'{action.character_name}@fake.com',
        )
    )

    assert result == Failure()
