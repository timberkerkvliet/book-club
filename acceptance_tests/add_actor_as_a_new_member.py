from __future__ import annotations

from dataclasses import dataclass

from screenplay.actor_name import ActorName
from screenplay.action import Action
from screenplay.notes import Note, NoteBook, NoteFinder
from add_a_new_member import AddNewMemberCommand
from request_handler import handle_command


@dataclass(frozen=True)
class IAddedAMember(Note):
    member_name: str


class AddActorAsANewMember(Action):
    def __init__(self, new_member: ActorName):
        self._new_member_name = new_member

    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        await handle_command(
            AddNewMemberCommand(
                name=self._new_member_name,
                mail_address='a@a.com',
            )
        )

        actor_note_book.write(IAddedAMember(member_name=self._new_member_name))
