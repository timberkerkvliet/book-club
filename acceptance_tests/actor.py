from __future__ import annotations

from acceptance_tests.actor_name import ActorName
from acceptance_tests.expectation import Expectation
from acceptance_tests.notes import NoteBook, NoteFinder
from acceptance_tests.action import Action


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

    def performs(self, *interactions: Action) -> None:
        for interaction in interactions:
            self._add_part(
                interaction.execute(
                    note_finder=self._note_finder,
                    actor_note_book=self._note_book
                )
            )

    def expects(self, *expectations: Expectation) -> None:
        for expectation in expectations:
            self._add_part(
                expectation.verify(
                    note_finder=self._note_finder,
                )
            )
