from __future__ import annotations

from screenplay.actor_name import ActorName
from screenplay.expectation import Expectation
from screenplay.notes import NoteRecords, NoteFinder
from screenplay.action import Action


class Actor:
    def __init__(
        self,
        name: ActorName,
        note_records: NoteRecords,
        add_part
    ) -> None:
        self._name = name
        self._note_records = note_records
        self._add_part = add_part

    @property
    def name(self) -> ActorName:
        return self._name

    def performs(self, *interactions: Action) -> None:
        for interaction in interactions:
            self._add_part(
                interaction.execute(
                    actor_name=self._name,
                    note_finder=self._note_records,
                    note_writer=self._note_records.get_writer_for(self._name)
                )
            )

    def expects(self, *expectations: Expectation) -> None:
        for expectation in expectations:
            self._add_part(
                expectation.verify(
                    actor_name=self._name,
                    note_finder=self._note_records,
                )
            )
