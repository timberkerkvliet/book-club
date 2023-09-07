from __future__ import annotations

from contextlib import asynccontextmanager

from acceptance_tests.actor import Actor
from acceptance_tests.actor_name import ActorName
from acceptance_tests.notes import NoteBookCollection


class Stage:
    def __init__(self):
        self._parts = []
        self._note_book_collection = NoteBookCollection()

    def actor_named(self, name: ActorName) -> Actor:
        actors_note_book = self._note_book_collection.add_notebook_for(name)

        return Actor(
            name=name,
            note_book=actors_note_book,
            note_finder=self._note_book_collection,
            add_part=self._parts.append
        )

    async def execute(self) -> None:
        for part in self._parts:
            await part


@asynccontextmanager
async def executable_spec() -> Stage:
    stage = Stage()
    yield stage
    await stage.execute()
