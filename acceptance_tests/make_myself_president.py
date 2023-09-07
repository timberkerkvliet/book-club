from __future__ import annotations

from screenplay.action import Action
from screenplay.notes import NoteBook, NoteFinder


class MakeMyselfPresident(Action):
    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        pass
