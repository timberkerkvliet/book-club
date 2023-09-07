from __future__ import annotations

from screenplay.expectation import Expectation
from screenplay.notes import NoteFinder
from app import app_mail_client


class WelcomeReceived(Expectation):
    async def verify(
        self,
        note_finder: NoteFinder
    ):
        mail_fake = app_mail_client()

        assert 'Welcome' in mail_fake.mails['a@a.com']
