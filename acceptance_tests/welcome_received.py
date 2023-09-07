from __future__ import annotations

from acceptance_tests.actor import Actor
from acceptance_tests.part import Part
from acceptance_tests.notes import NoteBook


class WelcomeReceived(Part):
    async def execute(
        self,
        note_book: NoteBook,
        actor: Actor
    ):
        mail_address_note = note_book.get_note(MyMailAddressIs)

        assert mail_fake.has_mail_for(mail_address_note.mail_address)
