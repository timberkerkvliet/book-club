from __future__ import annotations

from abc import ABC, abstractmethod

from acceptance_tests.notes import NoteBook, NoteFinder


class Expectation(ABC):
    @abstractmethod
    async def verify(
        self,
        note_finder: NoteFinder
    ):
        ...
