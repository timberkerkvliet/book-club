from __future__ import annotations

from dataclasses import dataclass

from book_club.app_context import AppContext
from book_club.mail_client import fake_mail_client
from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.prop import Props


@dataclass
class NewReadNotificationReceived(Assertion):
    book_name: str


@executes(NewReadNotificationReceived)
async def welcome_received(action: NewReadNotificationReceived, actor: Actor, stage_props: Props):
    app_context = await stage_props(AppContext)
    mail_fake = await fake_mail_client(app_context)
    address = f'{actor.character_name}@fake.com'
    assert action.book_name in mail_fake.mails[address]