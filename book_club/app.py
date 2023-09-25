from contextlib import asynccontextmanager
from typing import AsyncGenerator

from book_club.app_context import AppContext
from book_club.authenticate import authenticate
from book_club.request_handler import command_handlers, query_handlers, request_handler
from book_club.starlette_adapter import starlette_server, StarletteRequestHandler


@asynccontextmanager
async def app(is_fake: bool = False) -> AsyncGenerator[AppContext, None]:
    context = AppContext(is_fake=is_fake)
    async with context:
        if not is_fake:
            await context.join(
                starlette_server(
                    adapter=StarletteRequestHandler(
                        request_handler=request_handler(context),
                        authenticator=authenticate,
                        command_types=set(command_handlers().keys()),
                        query_types=set(query_handlers().keys())
                    ),
                    host='0.0.0.0',
                    port=80
                )
            )
        yield context
