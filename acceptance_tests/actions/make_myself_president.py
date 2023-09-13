from __future__ import annotations

from pyplay.action import Action
from pyplay.action_executor import executes


class MakeMyselfPresident(Action):
    pass


@executes(MakeMyselfPresident)
async def make_myself_president():
    pass
