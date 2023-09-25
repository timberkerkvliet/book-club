from dataclasses import dataclass

from book_club.failure import Failure
from book_club.mail import Mail
from book_club.mail_client import app_mail_client
from book_club.mail_address import MailAddress
from book_club.member_list.member import Member
from book_club.member_list.member_repository import member_repository
from book_club.name import Name
from book_club.request_context import RequestContext
from book_club.invoker import President


@dataclass(frozen=True)
class KickMember:
    name: str


async def kick_member(command: KickMember, request_context: RequestContext) -> None | Failure:
    if request_context.invoker != President():
        return Failure()

    repository = await member_repository(request_context)

    member_list = await repository.get_member_list()
    member_list.remove(command.name)

    await repository.save()
