from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from acceptance_tests.actions.member_joined import MemberJoined
from book_club.app_context import AppContext
from book_club.member_list.join_club import JoinClub
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class AddMember(Action):
    character_name: str


@executes(AddMember)
async def add_actor_as_new_member(
    action: AddMember,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)

    await handler.handle_command(
        invoker=get_invoker(log_book, actor.character_name),
        command=JoinClub(
            name=action.character_name,
            mail_address=f'{action.character_name}@fake.com',
        )
    )

    log_book.write_message(MemberJoined(member_name=action.character_name))
