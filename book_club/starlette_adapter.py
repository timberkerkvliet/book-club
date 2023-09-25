from asyncio import Event
from contextlib import asynccontextmanager
from typing import Awaitable, Callable

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from uvicorn import Config, Server

from book_club.request_context import Invoker
from book_club.request_handler import RequestHandler


class StarletteRequestHandler:
    def __init__(
        self,
        request_handler: RequestHandler,
        authenticator: Callable[[str], Awaitable[Invoker]],
        query_types: set,
        command_types: set
    ):
        self._request_handler = request_handler
        self._authenticator = authenticator
        self._query_types = query_types
        self._command_types = command_types

    async def handle_post(self, request: Request) -> JSONResponse:
        name = request.url.path.lstrip('/')

        command_types = {
            command_type
            for command_type in self._command_types
            if command_type.__name__ == name
        }

        if len(command_types) == 0:
            return JSONResponse({}, status_code=404)

        command_type = command_types.pop()
        data = await request.json()

        parts = request.headers.get('Authorization', '').split()
        token = parts[1] if len(parts) > 1 else None

        value = await self._request_handler.handle_command(
            invoker=await self._authenticator(token),
            command=command_type(**data)
        )

        return JSONResponse(value, status_code=200)

    async def handle_get(self, request: Request) -> JSONResponse:
        name = request.url.path.lstrip('/')

        query_types = {
            query_type
            for query_type in self._query_types
            if query_type.__name__ == name
        }

        if len(query_types) == 0:
            return JSONResponse({}, status_code=404)

        query_type = query_types.pop()
        data = request.query_params

        parts = request.headers.get('Authorization', '').split()
        token = parts[1] if len(parts) > 1 else None

        value = await self._request_handler.handle_query(
            invoker=await self._authenticator(token),
            query=query_type(**data)
        )

        return JSONResponse(value, status_code=200)


@asynccontextmanager
async def starlette_server(adapter: StarletteRequestHandler, host: str, port: int):
    starlette_app = Starlette()

    starlette_app.add_route(
        path='/{rest_of_path:path}',
        route=adapter.handle_post,
        methods=['POST']
    )
    starlette_app.add_route(
        path='/{rest_of_path:path}',
        route=adapter.handle_get,
        methods=['GET']
    )

    config = Config(starlette_app, host=host, port=port)
    server = Server(config)

    config = server.config
    if not config.loaded:
        config.load()

    server.lifespan = config.lifespan_class(config)
    try:
        await server.startup()
        yield None
    finally:
        await server.shutdown()
