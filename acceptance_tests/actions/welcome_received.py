from __future__ import annotations

from dataclasses import dataclass

from book_club.app_context import AppContext
from book_club.mail_client import fake_mail_client
from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.prop import Props


@dataclass(frozen=True)
class MyMailAddress:
    address: str


class WelcomeReceived(Assertion):
    pass


@executes(WelcomeReceived)
async def welcome_received(actor: Actor, stage_props: Props):
    app_context = await stage_props(AppContext)
    mail_fake = await fake_mail_client(app_context)
    address = f'{actor.character_name}@fake.com'
    assert 'Welcome' in mail_fake.mails[address]
