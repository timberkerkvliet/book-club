from asyncio import Event

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from uvicorn import Config, Server


class StarletteAdapter:
    def __init__(
        self,
        endpoint_map: dict,
        handler
    ):
        self._endpoint_map = endpoint_map
        self._handler = handler

    async def handle_command(self, request: Request) -> JSONResponse:
        command = self._endpoint_map[request.url.path.lstrip('/')]
        data = await request.json()
        value = await self._handler(command(**data))

        return JSONResponse(value, status_code=200)


async def run_server(adapter: StarletteAdapter, host: str, port: int):
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
