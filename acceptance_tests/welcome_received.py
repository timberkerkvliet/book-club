from __future__ import annotations

from acceptance_tests.expectation import Expectation
from acceptance_tests.notes import NoteFinder
from app import app_mail_client


class WelcomeReceived(Expectation):
    async def verify(
        self,
        note_finder: NoteFinder
    ):
        mail_fake = app_mail_client()

        assert 'Welcome' in mail_fake.mails['a@a.com']
