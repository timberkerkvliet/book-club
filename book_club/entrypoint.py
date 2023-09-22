import asyncio

from book_club.request_handler import request_handler
from book_club.starlette_adapter import StarletteRequestHandler, run_server


async def run():
    adapter = StarletteRequestHandler(
        request_handler=request_handler()
    )
    await run_server(adapter, host='0.0.0.0', port=80)


asyncio.run(run())
