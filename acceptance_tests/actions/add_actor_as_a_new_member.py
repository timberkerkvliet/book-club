from __future__ import annotations

from dataclasses import dataclass

from book_club.add_a_new_member import AddNewMemberCommand
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.log_book import LogBook, LogMessage


@dataclass(frozen=True)
class IAddedAMember(LogMessage):
    member_name: str


@dataclass
class AddActorAsANewMember(Action):
    new_member_name: str


@executes(AddActorAsANewMember)
async def add_actor_as_new_member(
    action: AddActorAsANewMember,
    log_book: LogBook
):
    handler = request_handler()
    await handler.handle_command(
        AddNewMemberCommand(
            name=action.new_member_name,
            mail_address=f'{action.new_member_name}@fake.com',
        )
    )

    log_book.write_message(IAddedAMember(member_name=action.new_member_name))
