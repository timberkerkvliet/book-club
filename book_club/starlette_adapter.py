from asyncio import Event
from contextlib import asynccontextmanager
from typing import Awaitable, Callable

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from uvicorn import Config, Server

from book_club.request_context import Invoker, President
from book_club.request_handler import RequestHandler


class StarletteRequestHandler:
    def __init__(
        self,
        request_handler: RequestHandler,
        authenticator: Callable[[str], Awaitable[Invoker]]
    ):
        self._request_handler = request_handler
        self._authenticator = authenticator

    async def handle_command(self, request: Request) -> JSONResponse:
        name = request.url.path.lstrip('/')

        command_types = {
            command_type
            for command_type in self._request_handler.command_types
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


@asynccontextmanager
async def starlette_server(adapter: StarletteRequestHandler, host: str, port: int):
    starlette_app = Starlette()

    starlette_app.add_route(
        path='/{rest_of_path:path}',
        route=adapter.handle_command,
        methods=['POST']
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
