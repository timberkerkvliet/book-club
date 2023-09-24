from __future__ import annotations

from dataclasses import dataclass

from book_club.app_context import AppContext
from book_club.president.add_a_new_member import AddNewMember
from book_club.request_context import President
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.log_book import LogBook, LogMessage
from pyplay.prop import Props


@dataclass(frozen=True)
class IAddedAMember(LogMessage):
    member_name: str


@dataclass
class AddActorAsANewMember(Action):
    new_member_name: str


@executes(AddActorAsANewMember)
async def add_actor_as_new_member(
    action: AddActorAsANewMember,
    log_book: LogBook,
    stage_props: Props
):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)
    await handler.handle_command(
        invoker=President(),
        command=AddNewMember(
            name=action.new_member_name,
            mail_address=f'{action.new_member_name}@fake.com',
        )
    )

    log_book.write_message(IAddedAMember(member_name=action.new_member_name))
