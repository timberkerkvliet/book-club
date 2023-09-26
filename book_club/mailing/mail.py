from dataclasses import dataclass

from book_club.mailing.mail_address import MailAddress


@dataclass(frozen=True)
class Mail:
    to: MailAddress
    subject: str
    content: str
