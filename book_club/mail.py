from dataclasses import dataclass

from book_club.mail_address import MailAddress


@dataclass(frozen=True)
class Mail:
    to: MailAddress
    subject: str
    content: str
