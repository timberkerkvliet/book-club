from __future__ import annotations

from pyplay.action import Action
from pyplay.name import Name
from typing import TYPE_CHECKING
from pyplay.act import Act

if TYPE_CHECKING:
    from pyplay.play import Play


class Character:
    def __init__(self, name: Name, play: Play):
        self._name = name
        self._play = play

    def performs(self, *actions: Action) -> Character:
        for action in actions:
            self._play.append_act(
                Act(character=self._name, action=action)
            )
        return self

    def asserts(self, *assertions) -> Character:
        return self.performs(*assertions)

    @property
    def name(self) -> Name:
        return self._name
