from asyncio import Event
from contextlib import asynccontextmanager
from typing import Awaitable, Callable

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from uvicorn import Config, Server

from book_club.app_context import app_resource, AppContext
from book_club.authenticate import authenticate
from book_club.command_handlers import command_handlers

from book_club.invoker import Invoker
from book_club.query_handlers import query_handlers
from book_club.request_handler import RequestHandler, request_handler


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

    async def _handle_request(
        self,
        request: Request,
        request_types: set,
        data,
        handler
    ) -> JSONResponse:
        name = request.url.path.lstrip('/')

        request_types = {
            request_type
            for request_type in request_types
            if request_type.__name__ == name
        }

        if len(request_types) == 0:
            return JSONResponse({}, status_code=404)

        request_type = request_types.pop()

        parts = request.headers.get('Authorization', '').split()
        token = parts[1] if len(parts) > 1 else None

        value = await handler(
            await self._authenticator(token),
            request_type(**data)
        )

        return JSONResponse(value, status_code=200)

    async def handle_post(self, request: Request) -> JSONResponse:
        return await self._handle_request(
            request=request,
            request_types=self._command_types,
            data=await request.json(),
            handler=self._request_handler.handle_command
        )

    async def handle_get(self, request: Request) -> JSONResponse:
        return await self._handle_request(
            request=request,
            request_types=self._query_types,
            data=dict(request.query_params),
            handler=self._request_handler.handle_query
        )


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


@app_resource
async def starlette_resource(app_context: AppContext):
    server = starlette_server(
        adapter=StarletteRequestHandler(
            request_handler=request_handler(app_context),
            authenticator=authenticate,
            command_types=set(command_handlers().keys()),
            query_types=set(query_handlers().keys())
        ),
        host='0.0.0.0',
        port=80
    )
    async with server:
        yield None
