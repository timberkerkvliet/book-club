from abc import ABC, abstractmethod
from typing import AsyncGenerator

from book_club.app_context import app_resource
from book_club.member_list.member import Member, MemberList
from book_club.request_context import RequestContext, request_resource


class MemberRepository(ABC):
    @abstractmethod
    async def get_member_list(self) -> MemberList:
        ...

    @abstractmethod
    async def save(self) -> None:
        ...


class InMemoryMemberRepository(MemberRepository):
    _member_list = MemberList(set())

    def __init__(self):
        self._list = MemberList(self._member_list)

    async def get_member_list(self) -> MemberList:
        return self._list

    async def save(self) -> None:
        InMemoryMemberRepository._member_list = self._list


@request_resource
async def member_repository(request_context: RequestContext) -> AsyncGenerator[MemberRepository, None]:
    yield InMemoryMemberRepository()
