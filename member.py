from dataclasses import dataclass

from mail_address import MailAddress
from name import Name


@dataclass
class Member:
    name: Name
    mail_address: MailAddress
