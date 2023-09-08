from __future__ import annotations

from dataclasses import dataclass

from screenplay.actor_name import ActorName
from screenplay.expectation import Expectation
from screenplay.notes import NoteFinder
from app import app_mail_client


@dataclass(frozen=True)
class MyMailAddress:
    address: str


class WelcomeReceived(Expectation):
    async def verify(
        self,
        actor_name: ActorName,
        note_finder: NoteFinder
    ):
        mail_fake = app_mail_client()

        my_mail_address = note_finder\
            .find_notes_of(actor_name)\
            .find_note_type(MyMailAddress)\
            .one()

        assert 'Welcome' in mail_fake.mails[my_mail_address]
