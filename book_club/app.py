from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncGenerator

from book_club.app_context import AppContext
from book_club.member_repository import InMemoryMemberRepository


@lru_cache
def app_member_repository():
    return InMemoryMemberRepository()


@asynccontextmanager
async def app(is_fake: bool = False) -> AsyncGenerator[AppContext, None]:
    context = AppContext(is_fake=is_fake)
    async with context:
        yield context
