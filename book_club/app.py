from contextlib import asynccontextmanager
from typing import AsyncGenerator

from book_club.app_context import AppContext


@asynccontextmanager
async def app(is_fake: bool = False) -> AsyncGenerator[AppContext, None]:
    context = AppContext(is_fake=is_fake)
    async with context:
        yield context
