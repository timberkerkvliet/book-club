from dataclasses import dataclass

from book_club.failure import Failure
from book_club.member_list.member_repository import request_member_repository
from book_club.request_context import RequestContext
from book_club.invoker import President


@dataclass(frozen=True)
class KickMember:
    name: str


async def kick_member(command: KickMember, request_context: RequestContext) -> None | Failure:
    if request_context.invoker != President():
        return Failure()

    repository = await request_member_repository(request_context)

    member_list = await repository.get_member_list()
    member_list.remove(command.name)

    await repository.save()
