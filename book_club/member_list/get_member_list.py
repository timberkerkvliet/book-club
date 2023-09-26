from dataclasses import dataclass

from book_club.member_list.member_repository import member_repository
from book_club.request_context import RequestContext


@dataclass(frozen=True)
class GetMemberList:
    pass


async def get_member_list(query: GetMemberList, request_context: RequestContext) -> set[str]:
    repository = await member_repository(request_context)

    return {member.name for member in await repository.get_member_list()}
