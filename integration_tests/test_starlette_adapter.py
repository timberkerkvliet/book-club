from contextlib import asynccontextmanager
from dataclasses import dataclass
from unittest import IsolatedAsyncioTestCase

import aiohttp
from book_club.app_context import AppContext
from book_club.request_context import RequestContext
from book_club.invoker import President, Member, Invoker
from book_club.request_handler import RequestHandler
from book_club.starlette import StarletteRequestHandler, starlette_server


@dataclass
class MyTestCommand:
    my_name: str


async def handle(request: MyTestCommand, request_context: RequestContext):
    return request.my_name


@dataclass
class AmIPresident:
    pass


async def handle_am_i_president(request: AmIPresident, request_context: RequestContext):
    return request_context.invoker == President()


@asynccontextmanager
async def server(adapter):
    async with starlette_server(adapter, host='0.0.0.0', port=8000):
        yield None


async def authenticate(token: str) -> Invoker:
    if token == 'president':
        return President()

    return Member(name='member')


class TestStarletteAdapter(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.adapter = StarletteRequestHandler(
            request_handler=RequestHandler(
                command_handlers={
                    MyTestCommand: handle,

                },
                query_handlers={
                    AmIPresident: handle_am_i_president
                },
                app_context=AppContext(is_fake=True)
            ),
            authenticator=authenticate,
            command_types={MyTestCommand},
            query_types={AmIPresident}
        )

    async def test_happy_path(self):
        async with server(self.adapter), aiohttp.ClientSession() as session:
            response = await session.post(
                url='http://localhost:8000/MyTestCommand',
                json={'my_name': 'Timber'}
            )

            self.assertEqual(
                await response.json(),
                'Timber'
            )

    async def test_get_404_on_non_existing_requests(self):
        async with server(self.adapter), aiohttp.ClientSession() as session:
            response = await session.get(url='http://localhost:8000/Anything')

            self.assertEqual(response.status, 404)

    async def test_request_without_presidential_key(self):
        async with server(self.adapter), aiohttp.ClientSession() as session:
            response = await session.get(url='http://localhost:8000/AmIPresident')

            self.assertEqual(await response.json(), False)

    async def test_request_with_presidential_key(self):
        async with server(self.adapter), aiohttp.ClientSession() as session:
            response = await session.get(
                url='http://localhost:8000/AmIPresident',
                headers={'Authorization': 'Bearer president'}
            )

            self.assertEqual(await response.json(), True)
