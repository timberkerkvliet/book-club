from __future__ import annotations

from abc import ABC, abstractmethod

from screenplay.notes import NoteFinder


class Expectation(ABC):
    @abstractmethod
    async def verify(
        self,
        note_finder: NoteFinder
    ):
        ...
