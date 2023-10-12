from __future__ import annotations

from dataclasses import dataclass

from book_club.app import App
from book_club.app_context import AppContext
from book_club.mailing.mail_client import fake_mail_client
from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.prop import Props


@dataclass
class BookElectionNotificationReceived(Assertion):
    book_names: list[str]


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

    assert 'Book Election' in mail.subject and all(name in mail.content for name in action.book_names)
