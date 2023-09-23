from contextlib import asynccontextmanager
from functools import lru_cache
from uuid import uuid4

from book_club.app_context import AppContext
from book_club.member_repository import InMemoryMemberRepository


@lru_cache
def app_member_repository():
    return InMemoryMemberRepository()


@asynccontextmanager
async def run_app(is_fake: bool = False):
    yield AppContext(
        id=uuid4(),
        is_fake=is_fake
    )
