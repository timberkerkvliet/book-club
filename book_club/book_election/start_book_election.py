from dataclasses import dataclass

from book_club.request_context import RequestContext


@dataclass
class StartBookElection:
    book_names: list[str]


async def start_book_election(command: StartBookElection, request_context: RequestContext) -> None:
    ...
