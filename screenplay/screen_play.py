from __future__ import annotations

from contextlib import asynccontextmanager

from screenplay.actor import Actor
from screenplay.actor_name import ActorName
from screenplay.notes import NoteRecords


class ScreenPlay:
    def __init__(self):
        self._parts = []
        self._note_records = NoteRecords()

    def actor_named(self, name: ActorName) -> Actor:
        return Actor(
            name=name,
            note_records=self._note_records,
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
