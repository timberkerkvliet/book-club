from typing import AsyncGenerator

from book_club.app_context import AppContext, app_resource
from book_club.mailing.fake_mail_client import fake_mail_client
from book_club.mailing.mail_client import MailClient
from book_club.mailing.send_grid_client import send_grid_mail_client


@app_resource
async def app_mail_client(app: AppContext) -> AsyncGenerator[MailClient, None]:
    if app.is_fake():
        yield await fake_mail_client(app)
    else:
        yield await send_grid_mail_client(app)
