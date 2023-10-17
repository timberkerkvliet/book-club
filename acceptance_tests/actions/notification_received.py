from __future__ import annotations

from dataclasses import dataclass

from book_club.app import App
from book_club.app_context import AppContext
from book_club.mailing.fake_mail_client import fake_mail_client
from pyplay.action import Expectation
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.prop import Props


class NotificationReceived(Expectation):
    def __init__(self):
        self.subject_contains = []
        self.content_contains = []

    def with_subject_containing(self, *pieces: str) -> NotificationReceived:
        self.subject_contains += pieces
        return self

    def with_content_containing(self, *pieces: str) -> NotificationReceived:
        self.content_contains += pieces
        return self


@executes(NotificationReceived)
async def notification_received(
    action: NotificationReceived,
    actor: Actor,
    stage_props: Props
):
    app = await stage_props(App)
    mail_fake = await fake_mail_client(app.context)
    address = f'{actor.character_name}@fake.com'
    mail = mail_fake.get_last_mail_sent_to(address)

    assert all(piece in mail.subject for piece in action.subject_contains)
    assert all(name in mail.content for name in action.content_contains)
