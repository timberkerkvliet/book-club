from book_club.mailing.mail import Mail
from book_club.mailing.mail_address import MailAddress
from book_club.mailing.mail_client import MailClient
from book_club.member_list.member_repository import MemberRepository


async def mail_all_members(
    mail_client: MailClient,
    member_repository: MemberRepository,
    subject: str,
    content: str
) -> None:
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
