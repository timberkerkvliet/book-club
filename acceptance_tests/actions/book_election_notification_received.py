from __future__ import annotations

from dataclasses import dataclass

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
    app_context = await stage_props(AppContext)
    mail_fake = await fake_mail_client(app_context)
    address = f'{actor.character_name}@fake.com'
    assert all(name in mail_fake.mails[address] for name in action.book_names)
