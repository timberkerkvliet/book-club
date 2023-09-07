from __future__ import annotations

from typing import NewType

from acceptance_tests.notes import NoteBook, NoteFinder
from acceptance_tests.part import Part


ActorName = NewType('ActorName', str)


class Actor:
    def __init__(
        self,
        name: ActorName,
        note_book: NoteBook,
        note_finder: NoteFinder,
        add_part
    ) -> None:
        self._name = name
        self._note_book = note_book
        self._note_finder = note_finder
        self._add_part = add_part

    def performs(self, *interactions: Part) -> None:
        for interaction in interactions:
            self._add_part(
                interaction.execute(
                    note_finder=self._note_finder,
                    actor_note_book=self._note_book
                )
            )

    def expects(self, *assertions: Part) -> None:
        for assertion in assertions:
            self._add_part(
                assertion.execute(
                    public_note_book=self._public_note_book,
                    actor_note_book=self._private_note_book
                )
            )
