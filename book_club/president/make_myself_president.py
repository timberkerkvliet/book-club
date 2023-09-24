from  __future__ import annotations
from dataclasses import dataclass

from book_club.app_context import AppContext
from book_club.failure import Failure


@dataclass(frozen=True)
class MakeMyselfPresident:
    pass


async def make_myself_president(command: MakeMyselfPresident, app_context: AppContext) -> None | Failure:
    return Failure()
