from __future__ import annotations

from acceptance_tests.actor_name import ActorName
from acceptance_tests.notes import NoteBook, NoteFinder
from acceptance_tests.part import Part


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

    @property
    def name(self) -> ActorName:
        return self._name

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
                    note_finder=self._note_finder,
                    actor_note_book=self._note_book
                )
            )
