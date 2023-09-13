from __future__ import annotations

from dataclasses import dataclass

from app import app_mail_client
from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor


@dataclass(frozen=True)
class MyMailAddress:
    address: str


class WelcomeReceived(Assertion):
    pass


@executes(WelcomeReceived)
async def welcome_received(actor: Actor):
    mail_fake = app_mail_client()
    address = f'{actor.character_name}@fake.com'
    assert 'Welcome' in mail_fake.mails[address]
