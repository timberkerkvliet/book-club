from __future__ import annotations

from dataclasses import dataclass

from acceptance_tests.actions.become_president import MyInvokerIs
from acceptance_tests.actions.get_invoker import get_invoker
from book_club.app import App
from book_club.app_context import AppContext
from book_club.member_list.get_member_list import GetMemberList
from book_club.request_handler import request_handler

from pyplay.action import Expectation
from pyplay.action_executor import executes
from pyplay.actor import Actor
from pyplay.log_book import LogBook
from pyplay.prop import Props


@dataclass(frozen=True)
class MyMailAddress:
    address: str


@dataclass
class IsAMember(Expectation):
    member_name: str


@executes(IsAMember)
async def welcome_received(action: IsAMember, actor: Actor, stage_props: Props, log_book: LogBook):
    app = await stage_props(App)
    handler = request_handler(app.context)

    member_list = await handler.handle_query(
        invoker=get_invoker(log_book=log_book, character_name=actor.character_name),
        query=GetMemberList()
    )

    assert action.member_name in member_list
