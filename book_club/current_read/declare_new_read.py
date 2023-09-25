from dataclasses import dataclass

from book_club.mail import Mail
from book_club.mail_client import app_mail_client
from book_club.member_list.member_repository import member_repository
from book_club.request_context import RequestContext


@dataclass
class DeclareNewRead:
    book_name: str


async def declare_current_book(command: DeclareNewRead, request_context: RequestContext) -> None:
    mail_client = await app_mail_client(request_context.app_context)

    repository = await member_repository(request_context)
    member_list = await repository.get_member_list()

    for member in member_list:
        await mail_client.send(
            mail=Mail(
                to=member.mail_address,
                subject='New Read',
                content=f'We will read {command.book_name}'
            )
        )
