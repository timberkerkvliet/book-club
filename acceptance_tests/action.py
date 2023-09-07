from __future__ import annotations

from abc import ABC, abstractmethod

from acceptance_tests.notes import NoteBook, NoteFinder


class Action(ABC):
    @abstractmethod
    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        ...
