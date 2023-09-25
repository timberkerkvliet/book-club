from __future__ import annotations

from dataclasses import dataclass

from book_club.request_context import Invoker, President
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.log_book import LogBook, LogMessage


class BecomePresident(Action):
    pass


@dataclass
class MyInvokerIs(LogMessage):
    invoker: Invoker


@executes(BecomePresident)
async def make_myself_president(log_book: LogBook):
    log_book.write_message(MyInvokerIs(invoker=President()))
