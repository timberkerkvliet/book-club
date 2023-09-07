from __future__ import annotations

from acceptance_tests.action import Action
from acceptance_tests.notes import NoteBook, NoteFinder


class MakeMyselfPresident(Action):
    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        pass
