from __future__ import annotations

from screenplay.action import Action
from screenplay.actor_name import ActorName
from screenplay.notes import NoteFinder, NoteWriter


class MakeMyselfPresident(Action):
    async def execute(
        self,
        actor_name: ActorName,
        note_finder: NoteFinder,
        note_writer: NoteWriter
    ):
        pass
