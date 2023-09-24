import os
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncGenerator

from book_club.app_context import AppContext, app_resource
from book_club.http_client_session import app_http_session
from book_club.mail_address import MailAddress


class MailClient(ABC):
    @abstractmethod
    async def send(self, to: MailAddress, body: str) -> None:
        ...


class FakeMailClient(MailClient):
    def __init__(self):
        self.mails: dict[MailAddress, str] = {}

    async def send(self, to: MailAddress, body: str) -> None:
        self.mails[to] = body


class SendGridClient(MailClient):
    def __init__(
        self,
        aiohttp_session,
        api_key: str,
        url: str,
        from_address: str
    ):
        self._aiohttp_session = aiohttp_session
        self._api_key = api_key
        self._url = url
        self._from_address = from_address

    async def send(self, to: MailAddress, body: str) -> None:
        self._aiohttp_session.post(
            headers={
                'Authorization': f'Bearer {self._api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'personalizations': [{
                    'to': [{'email': to}]
                }],
                'from': {
                    'email': self._from_address,
                    'name': 'Book Club'
                },
                'subject': 'Hey',
                'content': [{
                    'type': 'text/plain',
                    'value': body
                }]
            }
        )


@app_resource
@asynccontextmanager
async def fake_mail_client(app: AppContext):
    yield FakeMailClient()


@app_resource
@asynccontextmanager
async def real_mail_client(app_context: AppContext) -> AsyncGenerator[SendGridClient, None]:
    yield SendGridClient(
        aiohttp_session=await app_http_session(app_context),
        api_key=os.getenv('SEND_GRID_API_KEY', default=''),
        from_address=os.getenv('SEND_GRID_FROM_ADDRESS', default=''),
        url=os.getenv('SEND_GRID_URL', default='')
    )


@app_resource
@asynccontextmanager
async def app_mail_client(app: AppContext) -> AsyncGenerator[MailClient, None]:
    if app.is_fake():
        yield await fake_mail_client(app)
    else:
        yield await real_mail_client(app)
