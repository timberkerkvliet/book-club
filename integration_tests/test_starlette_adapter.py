import asyncio
from dataclasses import dataclass
from time import sleep
from unittest import IsolatedAsyncioTestCase

import aiohttp
import requests

from book_club.starlette_adapter import StarletteAdapter, run_server


@dataclass
class MyTestCommand:
    my_name: str


async def handle(request: MyTestCommand):
    return request.my_name


class TestStarletteAdapter(IsolatedAsyncioTestCase):
    async def test_happy_path(self):
        adapter = StarletteAdapter(
            endpoint_map={'my_test_thing': MyTestCommand},
            handler=handle
        )
        asyncio.create_task(run_server(adapter, host='0.0.0.0', port=8000))
        await asyncio.sleep(1)

        async with aiohttp.ClientSession() as session:
            response = await session.post(
                url='http://localhost:8000/my_test_thing',
                json={'my_name': 'Timber'}
            )

            self.assertEqual(
                await response.json(),
                'Timber'
            )
