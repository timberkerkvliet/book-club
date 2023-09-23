from dataclasses import dataclass

from book_club.app import app_mail_client
from book_club.mail_address import MailAddress
from book_club.member import Member
from book_club.name import Name


@dataclass(frozen=True)
class AddNewMember:
    name: str
    mail_address: str


async def add_a_new_member(command: AddNewMember) -> None:
    address = MailAddress(command.mail_address)
    member = Member(
        name=Name(command.name),
        mail_address=address
    )

    await app_mail_client().send(
        to=address,
        body=f'Welcome {member.name}!'
    )
