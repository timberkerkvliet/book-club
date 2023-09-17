from abc import ABC, abstractmethod

from member import Member


class MemberRepository(ABC):
    @abstractmethod
    async def add_member(self, member: Member) -> None:
        ...

    @abstractmethod
    async def get_all_members(self) -> set[Member]:
        ...


class InMemoryMemberRepository(MemberRepository):
    def __init__(self):
        self._members = []

    async def add_member(self, member) -> None:
        self._members.append(member)

    async def get_all_members(self) -> list[Member]:
        return self._members
