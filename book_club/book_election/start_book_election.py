from dataclasses import dataclass

from book_club.failure import Failure
from book_club.invoker import President
from book_club.mailing.mail_all_members import mail_all_members
from book_club.mailing.mail_client import app_mail_client
from book_club.member_list.member_repository import request_member_repository
from book_club.request_context import RequestContext


@dataclass
class StartBookElection:
    book_names: list[str]


async def start_book_election(command: StartBookElection, request_context: RequestContext) -> None | Failure:
    if request_context.invoker != President():
        return Failure()

    await mail_all_members(
        mail_client=await app_mail_client(request_context.app_context),
        member_repository=await request_member_repository(request_context),
        subject='New Book Election',
        content='\n'.join(command.book_names)
    )
