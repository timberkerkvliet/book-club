from book_club.mailing.mail import Mail
from book_club.mailing.mail_address import MailAddress
from book_club.mailing.mail_client import MailClient


async def mail_all(
    mail_client: MailClient,
    mail_addresses: set[MailAddress],
    subject: str,
    content: str
) -> None:
    for mail_address in mail_addresses:
        await mail_client.send(
            mail=Mail(
                to=mail_address,
                subject=subject,
                content=content
            )
        )
