from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from acceptance_tests.actions.invoke_api import invoke_api
from acceptance_tests.actions.member_joined import MemberJoined
from book_club.app import App
from book_club.app_context import AppContext
from book_club.failure import Failure
from book_club.member_list.add_member import AddMember as AddMemberCommand
from pyplay.action import Action
from pyplay.action_executor import FailedAction, executes
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
    result = await invoke_api(
        command=AddMemberCommand(
            name=action.character_name,
            mail_address=f'{action.character_name}@fake.com',
        ),
        app=await stage_props(App),
        log_book=log_book,
        character_name=actor.character_name,
    )
    if result == Failure():
        return FailedAction()

    log_book.write_message(MemberJoined(member_name=action.character_name))
