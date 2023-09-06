from abc import ABC, abstractmethod


class MemberRepository(ABC):
    @abstractmethod
    async def add_member(self, member) -> None:
        ...
