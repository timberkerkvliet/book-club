from abc import ABC, abstractmethod
from functools import lru_cache

from book_club.adapter_type import AppContext
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
    async def send(self, to: MailAddress, body: str) -> None:
        pass


@lru_cache
def fake_mail_client(app: AppContext):
    return FakeMailClient()


@lru_cache
def real_mail_client(app: AppContext):
    return SendGridClient()


@lru_cache
def app_mail_client(app: AppContext) -> MailClient:
    if app.is_fake:
        return fake_mail_client(app)

    return real_mail_client(app)
