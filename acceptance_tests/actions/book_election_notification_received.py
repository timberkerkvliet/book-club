from __future__ import annotations

from dataclasses import dataclass

from book_club.app import App
from book_club.app_context import AppContext
from book_club.mailing.mail_client import fake_mail_client
from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.prop import Props


class BookElectionNotificationReceived(Assertion):
    def __init__(self):
        self.subject_contains = []
        self.content_contains = []

    def and_subject_contains(self, *pieces: str) -> BookElectionNotificationReceived:
        self.subject_contains += pieces
        return self

    def and_content_contains(self, *pieces: str) -> BookElectionNotificationReceived:
        self.content_contains += pieces
        return self


@executes(BookElectionNotificationReceived)
async def book_election_notification_received(
    action: BookElectionNotificationReceived,
    actor: Actor,
    stage_props: Props
):
    app = await stage_props(App)
    mail_fake = await fake_mail_client(app.context)
    address = f'{actor.character_name}@fake.com'
    mail = mail_fake.last_mail_to(address)

    assert all(piece in mail.subject for piece in action.subject_contains)
    assert all(name in mail.content for name in action.content_contains)
