from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncGenerator

from book_club.app_context import AppContext, app_resource
from book_club.authenticate import authenticate
from book_club.query_handlers import query_handlers
from book_club.command_handlers import command_handlers
from book_club.request_handler import RequestHandler
from book_club.starlette_adapter import starlette_server, StarletteRequestHandler


@app_resource
def starlette_resource(app_context):
    return starlette_server(
        adapter=StarletteRequestHandler(
            request_handler=request_handler(app_context),
            authenticator=authenticate,
            command_types=set(command_handlers().keys()),
            query_types=set(query_handlers().keys())
        ),
        host='0.0.0.0',
        port=80
    )


@asynccontextmanager
async def app(is_fake: bool = False) -> AsyncGenerator[AppContext, None]:
    context = AppContext(is_fake=is_fake)
    async with context:
        if not is_fake:
            await starlette_resource(context)
        yield context


@lru_cache
def request_handler(app_context: AppContext) -> RequestHandler:
    return RequestHandler(
        command_handlers=command_handlers(),
        query_handlers=query_handlers(),
        app_context=app_context
    )
