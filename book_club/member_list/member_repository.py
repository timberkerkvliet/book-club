from abc import ABC, abstractmethod
from typing import AsyncGenerator

from book_club.app_context import app_resource
from book_club.member_list.member import Member
from book_club.request_context import RequestContext, request_resource


class MemberRepository(ABC):
    @abstractmethod
    async def get_member_list(self) -> set[Member]:
        ...

    @abstractmethod
    async def save(self) -> None:
        ...


class InMemoryMemberRepository(MemberRepository):
    _members = []

    def __init__(self):
        self._list = None

    async def get_member_list(self) -> list[Member]:
        self._list = list(InMemoryMemberRepository._members)
        return self._list

    async def save(self) -> None:
        InMemoryMemberRepository._members = self._list


@request_resource
async def member_repository(request_context: RequestContext) -> AsyncGenerator[MemberRepository, None]:
    yield InMemoryMemberRepository()
