import os
from typing import AsyncGenerator

from book_club.app_context import AppContext, app_resource
from book_club.http_client_session import app_http_session
from book_club.mailing.mail import Mail
from book_club.mailing.mail_client import MailClient


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

    async def send(self, mail: Mail) -> None:
        await self._aiohttp_session.post(
            url=self._url,
            headers={
                'Authorization': f'Bearer {self._api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'personalizations': [
                    {
                        'to': [{'email': mail.to}]
                    }
                ],
                'from': {
                    'email': self._from_address,
                    'name': 'Book Club'
                },
                'subject': mail.subject,
                'content': [
                    {
                        'type': 'text/plain',
                        'value': mail.content
                    }
                ]
            }
        )


@app_resource
async def send_grid_mail_client(app_context: AppContext) -> AsyncGenerator[SendGridClient, None]:
    yield SendGridClient(
        aiohttp_session=await app_http_session(app_context),
        api_key=os.getenv('SEND_GRID_API_KEY', default=''),
        from_address=os.getenv('SEND_GRID_FROM_ADDRESS', default=''),
        url=os.getenv('SEND_GRID_URL', default='')
    )
