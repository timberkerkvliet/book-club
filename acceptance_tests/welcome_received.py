from __future__ import annotations

from acceptance_tests.part import Part
from acceptance_tests.notes import NoteBook, NoteFinder
from app import app_mail_client


class WelcomeReceived(Part):
    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        mail_fake = app_mail_client()

        assert 'Welcome' in mail_fake.mails['a@a.com']
