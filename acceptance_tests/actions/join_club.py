from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from book_club.app_context import AppContext
from book_club.member_list.join_club import JoinClub
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook, LogMessage
from pyplay.prop import Props


@dataclass(frozen=True)
class MemberJoined(LogMessage):
    member_name: str


@dataclass
class LetCharacterJoinClub(Action):
    character_name: str


@executes(LetCharacterJoinClub)
async def add_actor_as_new_member(
    action: LetCharacterJoinClub,
    log_book: LogBook,
    stage_props: Props,
    actor: Actor
):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)

    invoker_log = log_book.find().by_actor(actor.character_name).by_type(MyInvokerIs).one()

    await handler.handle_command(
        invoker=invoker_log.invoker,
        command=JoinClub(
            name=action.character_name,
            mail_address=f'{action.character_name}@fake.com',
        )
    )

    log_book.write_message(MemberJoined(member_name=action.character_name))
