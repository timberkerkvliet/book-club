from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from book_club.app import App
from book_club.app_context import AppContext
from book_club.member_list.get_member_list import GetMemberList
from book_club.request_handler import request_handler

from pyplay.action import Expectation
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass
class IsNotAMember(Expectation):
    member_name: str


@executes(IsNotAMember)
async def welcome_received(action: IsNotAMember, actor: Actor, stage_props: Props, log_book: LogBook):
    app = await stage_props(App)
    handler = request_handler(app.context)

    invoker_log = log_book.find().by_actor(actor.character_name).by_type(MyInvokerIs).one()

    member_list = await handler.handle_query(
        invoker=invoker_log.invoker,
        query=GetMemberList()
    )

    assert action.member_name not in member_list
