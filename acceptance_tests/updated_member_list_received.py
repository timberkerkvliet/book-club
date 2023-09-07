from __future__ import annotations

from acceptance_tests.part import Part
from acceptance_tests.notes import NoteBook, NoteFinder


class UpdatedMemberListReceived(Part):
    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        member_added_note = note_finder.find_notes()

        assert mail_fake.has_mail_for(mail_address_note.mail_address)