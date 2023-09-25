from dataclasses import dataclass

from book_club.mail import Mail
from book_club.mail_client import app_mail_client
from book_club.mail_address import MailAddress
from book_club.member_list.member import Member
from book_club.member_list.member_repository import member_repository
from book_club.name import Name
from book_club.request_context import RequestContext


@dataclass(frozen=True)
class LeaveClub:
    name: str


async def leave_club(command: LeaveClub, request_context: RequestContext) -> None:
    repository = await member_repository(request_context)

    member_list = await repository.get_member_list()
    member_list.remove(command.name)

    await repository.save()
