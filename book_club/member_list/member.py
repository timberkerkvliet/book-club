from dataclasses import dataclass
from typing import Iterable

from book_club.mail_address import MailAddress
from book_club.name import Name


@dataclass(frozen=True)
class Member:
    name: Name
    mail_address: MailAddress


class MemberList:
    def __init__(self, members: Iterable[Member]) -> None:
        self._members = set(members)

    def add(self, member):
        self._members.add(member)

    def remove(self, name: str) -> None:
        self._members = {
            member for member in self._members if member.name != name
        }

    def __iter__(self):
        return iter(self._members)

    def __len__(self) -> int:
        return len(self._members)
