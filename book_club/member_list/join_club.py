from dataclasses import dataclass

from book_club.mail import Mail
from book_club.mail_client import app_mail_client
from book_club.mail_address import MailAddress
from book_club.member_list.member import Member
from book_club.member_list.member_repository import member_repository
from book_club.name import Name
from book_club.request_context import RequestContext


@dataclass(frozen=True)
class JoinClub:
    name: str
    mail_address: str


async def join_club(command: JoinClub, request_context: RequestContext) -> None:
    address = MailAddress(command.mail_address)
    repository = await member_repository(request_context)
    member_list = await repository.get_member_list()
    new_member = Member(
            name=Name(command.name),
            mail_address=address
        )
    member_list.add(new_member)

    mail_client = await app_mail_client(request_context.app_context)

    await repository.save()

    await mail_client.send(
        mail=Mail(
            to=address,
            subject='Welcome to the book club',
            content=f'Welcome {new_member.name}!'
        )
    )
