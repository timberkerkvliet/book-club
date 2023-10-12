from book_club.mailing.mail import Mail
from book_club.mailing.mail_address import MailAddress
from book_club.mailing.mail_client import MailClient, app_mail_client
from book_club.member_list.member_repository import MemberRepository, request_member_repository
from book_club.request_context import RequestContext


async def mail_all_members(
    request_context: RequestContext,
    subject: str,
    content: str
) -> None:

    mail_client = await app_mail_client(request_context.app_context)
    member_repository = await request_member_repository(request_context)

    mail_addresses = {
        member.mail_address
        for member in await member_repository.get_member_list()
    }
    for mail_address in mail_addresses:
        await mail_client.send(
            mail=Mail(
                to=mail_address,
                subject=subject,
                content=content
            )
        )
