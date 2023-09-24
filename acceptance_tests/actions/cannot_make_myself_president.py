from __future__ import annotations

from book_club.app_context import AppContext
from book_club.president.make_myself_president import MakeMyselfPresident
from book_club.request_handler import request_handler
from book_club.failure import Failure
from pyplay.action import Assertion
from pyplay.action_executor import executes
from pyplay.prop import Props


class CanNotMakeMyselfPresident(Assertion):
    pass


@executes(CanNotMakeMyselfPresident)
async def can_not_make_myself_president(stage_props: Props):
    app_context = await stage_props(AppContext)
    handler = request_handler(app_context)
    result = await handler.handle_command(MakeMyselfPresident())

    assert isinstance(result, Failure)
