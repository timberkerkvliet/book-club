from asyncio import Event

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from uvicorn import Config, Server

from book_club.request_handler import RequestHandler


class StarletteRequestHandler:
    def __init__(
        self,
        request_handler: RequestHandler
    ):
        self._request_handler = request_handler

    async def handle_command(self, request: Request) -> JSONResponse:
        name = request.url.path.lstrip('/')

        command_types = {
            command_type
            for command_type in self._request_handler.command_types
            if command_type.__name__ == name
        }

        command_type = command_types.pop()
        data = await request.json()
        value = await self._request_handler.handle_command(command_type(**data))

        return JSONResponse(value, status_code=200)


async def run_server(adapter: StarletteRequestHandler, host: str, port: int):
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
        await Event().wait()
    finally:
        await server.shutdown()
