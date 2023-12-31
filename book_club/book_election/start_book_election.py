from dataclasses import dataclass

from book_club.failure import Failure
from book_club.invoker import President
from book_club.mailing.mail_all_members import mail_all_members
from book_club.request_context import RequestContext


@dataclass
class StartBookElection:
    candidates: list[str]


async def start_book_election(
    command: StartBookElection,
    request_context: RequestContext
) -> None | Failure:
    if request_context.invoker != President():
        return Failure()

    await mail_all_members(
        request_context=request_context,
        subject='Book Election',
        content='\n'.join(command.candidates)
    )




