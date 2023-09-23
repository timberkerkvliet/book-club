from dataclasses import dataclass

from book_club.adapter_type import AppContext
from book_club.mail_client import app_mail_client
from book_club.mail_address import MailAddress
from book_club.member import Member
from book_club.name import Name


@dataclass(frozen=True)
class AddNewMember:
    name: str
    mail_address: str


async def add_a_new_member(command: AddNewMember, app_context: AppContext) -> None:
    address = MailAddress(command.mail_address)
    member = Member(
        name=Name(command.name),
        mail_address=address
    )

    await app_mail_client(app_context).send(
        to=address,
        body=f'Welcome {member.name}!'
    )
