from dataclasses import dataclass

from book_club.mail_address import MailAddress
from book_club.name import Name


@dataclass
class Member:
    name: Name
    mail_address: MailAddress
