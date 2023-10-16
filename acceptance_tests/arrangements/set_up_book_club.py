from __future__ import annotations
from typing import Iterator

from acceptance_tests.actions.add_member import AddMember
from acceptance_tests.actions.become_president import BecomePresident
from pyplay.action import Action
from pyplay.character import Character


class SetUpBookClub:
    def __init__(self):
        self._members = []

    def with_member(self, character: Character) -> SetUpBookClub:
        self._members.append(character)
        return self

    def __iter__(self) -> Iterator[Action]:
        actions: list[Action] = [
            BecomePresident()
        ] + [
            AddMember(character.name) for character in self._members
        ]

        return iter(actions)
