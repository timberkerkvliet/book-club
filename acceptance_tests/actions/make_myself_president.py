from __future__ import annotations

from book_club.app_context import AppContext
from book_club.president.make_myself_president import MakeMyselfPresident
from book_club.request_context import President
from book_club.request_handler import request_handler
from pyplay.action import Action
from pyplay.action_executor import executes
from pyplay.prop import Props


class BecomePresident(Action):
    pass


@executes(BecomePresident)
async def make_myself_president(stage_props: Props):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)
    await handler.handle_command(
        invoker=President(),
        command=MakeMyselfPresident()
    )
