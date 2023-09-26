import os
import pickle
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from book_club.member_list.member import MemberList
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


class FileMemberRepository(MemberRepository):
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._list = None

    def _load_from_file(self) -> MemberList:
        if not os.path.isfile(self._file_path):
            return MemberList(set())
        with open(self._file_path, 'rb') as file:
            return pickle.load(file)

    async def get_member_list(self) -> MemberList:
        if self._list is None:
            self._list = self._load_from_file()
        return self._list

    async def save(self) -> None:
        with open(self._file_path, 'wb') as file:
            pickle.dump(self._list, file)


@request_resource
@asynccontextmanager
async def member_repository(request_context: RequestContext) -> AsyncGenerator[MemberRepository, None]:
    if request_context.app_context.is_fake():
        yield InMemoryMemberRepository()
    else:
        yield FileMemberRepository('/data/member_list')
