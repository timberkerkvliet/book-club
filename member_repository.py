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
        self._members = set()

    async def add_member(self, member) -> None:
        self._members.add(member)

    async def get_all_members(self) -> set[Member]:
        return self._members
