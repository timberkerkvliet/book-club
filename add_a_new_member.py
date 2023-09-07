from dataclasses import dataclass
from typing import NewType

from acceptance_tests.mail_client import MailClient
from mail_address import MailAddress
from member import Member
from member_repository import MemberRepository
from name import Name


@dataclass(frozen=True)
class AddNewMemberCommand:
    name: str
    mail_address: str


async def add_a_new_member(
    command: AddNewMemberCommand,
    member_repository: MemberRepository,
    mail_client: MailClient
) -> None:
    address = MailAddress(command.mail_address)
    member = Member(
        name=Name(command.name),
        mail_address=address
    )
    await member_repository.add_member(member)

    await mail_client.send(
        to=address,
        body=f'Welcome {member.name}!'
    )
