from __future__ import annotations

from contextlib import asynccontextmanager

from screenplay.actor import Actor
from screenplay.actor_name import ActorName
from screenplay.notes import NoteBookCollection


class ScreenPlay:
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
async def screenplay() -> ScreenPlay:
    stage = ScreenPlay()
    yield stage
    await stage.execute()
