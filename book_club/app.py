import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from book_club.app_context import AppContext
from book_club.request_context import Invoker, Member, President
from book_club.request_handler import request_handler
from book_club.starlette_adapter import starlette_server, StarletteRequestHandler


async def authenticate(token: str) -> Invoker:
    if token == os.getenv('PRESIDENTIAL_TOKEN', ''):
        return President()

    return Member()


@asynccontextmanager
async def app(is_fake: bool = False) -> AsyncGenerator[AppContext, None]:
    context = AppContext(is_fake=is_fake)
    async with context:
        if not is_fake:
            await context.join(
                starlette_server(
                    adapter=StarletteRequestHandler(
                        request_handler=request_handler(context),
                        authenticator=authenticate
                    ),
                    host='0.0.0.0',
                    port=80
                )
            )
        yield context
