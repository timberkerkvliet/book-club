
from contextlib import asynccontextmanager
from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase
from uuid import uuid4

import aiohttp
import requests

from book_club.app_context import AppContext
from book_club.request_handler import RequestHandler
from book_club.starlette_adapter import StarletteRequestHandler, starlette_server


@dataclass
class MyTestCommand:
    my_name: str


async def handle(request: MyTestCommand, app_context: AppContext):
    return request.my_name


@asynccontextmanager
async def server(adapter):
    async with starlette_server(adapter, host='0.0.0.0', port=8000):
        yield None


class TestStarletteAdapter(IsolatedAsyncioTestCase):
    async def test_happy_path(self):
        adapter = StarletteRequestHandler(
            request_handler=RequestHandler(
                command_handlers={
                    MyTestCommand: handle
                },
                app_context=AppContext(id=uuid4(), is_fake=True)
            )
        )
        async with server(adapter), aiohttp.ClientSession() as session:
            response = await session.post(
                url='http://localhost:8000/MyTestCommand',
                json={'my_name': 'Timber'}
            )

            self.assertEqual(
                await response.json(),
                'Timber'
            )

    async def test_get_404_on_non_existing_requests(self):
        adapter = StarletteRequestHandler(
            request_handler=RequestHandler(
                command_handlers={},
                app_context=AppContext(id=uuid4(), is_fake=True)
            )
        )
        async with server(adapter), aiohttp.ClientSession() as session:
            response = await session.post(url='http://localhost:8000/Anything')

            self.assertEqual(response.status, 404)
