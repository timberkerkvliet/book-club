from book_club.app_context import AppContext, app_resource
from book_club.mailing.mail import Mail
from book_club.mailing.mail_address import MailAddress
from book_club.mailing.mail_client import MailClient


class FakeMailClient(MailClient):
    def __init__(self):
        self._mails: dict[MailAddress, Mail] = {}

    def get_last_mail_sent_to(self, address: MailAddress) -> Mail:
        return self._mails[address]

    async def send(self, mail: Mail) -> None:
        self._mails[mail.to] = mail


@app_resource
async def fake_mail_client(app: AppContext):
    yield FakeMailClient()
