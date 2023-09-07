from __future__ import annotations

from acceptance_tests.part import Part
from acceptance_tests.notes import IAmPresident, NoteBook, NoteFinder


class MakeMyselfPresident(Part):
    async def execute(
        self,
        note_finder: NoteFinder,
        actor_note_book: NoteBook
    ):
        actor_note_book.write(IAmPresident(presidential_token='token'))
