from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.make_myself_president import MyInvokerIs
from book_club.app_context import AppContext
from book_club.mail_client import fake_mail_client
from book_club.member_list.get_member_list import GetMemberList
from book_club.request_handler import request_handler

from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass(frozen=True)
class MyMailAddress:
    address: str


@dataclass
class IsAMember(Assertion):
    member_name: str


@executes(IsAMember)
async def welcome_received(action: IsAMember, actor: Actor, stage_props: Props, log_book: LogBook):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)

    invoker_log = log_book.find().by_actor(actor.character_name).by_type(MyInvokerIs).one()

    list = await handler.handle_query(
        invoker=invoker_log.invoker,
        query=GetMemberList()
    )

    assert action.member_name in list
