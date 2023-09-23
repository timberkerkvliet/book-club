import asyncio
from dataclasses import dataclass
from time import sleep
from unittest import IsolatedAsyncioTestCase

import aiohttp
import requests

from book_club.request_handler import RequestHandler
from book_club.starlette_adapter import StarletteRequestHandler, run_server


@dataclass
class MyTestCommand:
    my_name: str


async def handle(request: MyTestCommand):
    return request.my_name


class TestStarletteAdapter(IsolatedAsyncioTestCase):
    async def test_happy_path(self):
        adapter = StarletteRequestHandler(
            request_handler=RequestHandler(
                command_handlers={
                    MyTestCommand: handle
                }
            )
        )
        task = asyncio.create_task(run_server(adapter, host='0.0.0.0', port=8000))
        try:
            await asyncio.sleep(1)

            async with aiohttp.ClientSession() as session:
                response = await session.post(
                    url='http://localhost:8000/MyTestCommand',
                    json={'my_name': 'Timber'}
                )

                self.assertEqual(
                    await response.json(),
                    'Timber'
                )
        finally:
            task.cancel()
            await asyncio.wait([task])

    async def test_get_404_on_non_existing_requests(self):
        adapter = StarletteRequestHandler(
            request_handler=RequestHandler(
                command_handlers={}
            )
        )
        task = asyncio.create_task(run_server(adapter, host='0.0.0.0', port=8000))
        try:
            await asyncio.sleep(1)

            async with aiohttp.ClientSession() as session:
                response = await session.post(url='http://localhost:8000/Anything')

                self.assertEqual(response.status, 404)
        finally:
            task.cancel()
            await asyncio.wait([task])
