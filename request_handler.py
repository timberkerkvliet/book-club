
from add_a_new_member import add_a_new_member
from app import app_mail_client, app_member_repository


async def handle_command(command) -> None:
    await add_a_new_member(
        command=command,
        member_repository=app_member_repository(),
        mail_client=app_mail_client()
    )
