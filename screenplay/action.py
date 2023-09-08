from __future__ import annotations

from abc import ABC, abstractmethod

from screenplay.actor_name import ActorName
from screenplay.notes import NoteFinder, NoteWriter


class Action(ABC):
    @abstractmethod
    async def execute(
        self,
        actor_name: ActorName,
        note_finder: NoteFinder,
        note_writer: NoteWriter
    ):
        ...
