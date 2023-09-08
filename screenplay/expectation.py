from __future__ import annotations

from abc import ABC, abstractmethod

from screenplay.actor_name import ActorName
from screenplay.notes import NoteFinder


class Expectation(ABC):
    @abstractmethod
    async def verify(
        self,
        actor_name: ActorName,
        note_finder: NoteFinder
    ):
        ...
