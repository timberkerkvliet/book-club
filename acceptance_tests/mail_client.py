from abc import ABC, abstractmethod

from mail_address import MailAddress


class MailClient(ABC):
    @abstractmethod
    async def send(self, to: MailAddress, body: str) -> None:
        ...


class FakeMailClient(MailClient):
    def __init__(self):
        self.mails: dict[MailAddress, str] = {}

    async def send(self, to: MailAddress, body: str) -> None:
        self.mails[to] = body
