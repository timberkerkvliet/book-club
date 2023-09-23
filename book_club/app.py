from contextlib import asynccontextmanager, AsyncExitStack
from functools import lru_cache
from typing import AsyncGenerator
from uuid import uuid4

from book_club.app_context import AppContext
from book_club.member_repository import InMemoryMemberRepository


@lru_cache
def app_member_repository():
    return InMemoryMemberRepository()


@asynccontextmanager
async def app(is_fake: bool = False) -> AsyncGenerator[AppContext, None]:
    context = AppContext(
        id=uuid4(),
        is_fake=is_fake,
        exit_stack=AsyncExitStack()
    )
    async with context.exit_stack:
        yield context
