from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actor import ActorName
from acceptance_tests.part import Part
from acceptance_tests.notes import MyNameIs, Note, NoteBook, NoteFinder
from add_a_new_member import AddNewMemberCommand
from app import request_handler
from request_handler import handle_command


@dataclass(frozen=True)
class IAddedAMember(Note):
    member_name: str


class AddActorAsANewMember(Part):
    def __init__(self, new_member: ActorName):
        self._new_member = new_member

    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        name_note = note_finder.find_notes_of(self._new_member).find_one_note(MyNameIs)

        await handle_command(
            AddNewMemberCommand(
                name=name_note.name,
                mail_address='a@a.com',
            )
        )

        actor_note_book.write(IAddedAMember(member_name=name_note.name))
