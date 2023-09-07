from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, TypeVar

from acceptance_tests.actor_name import ActorName


class Note:
    pass


class NoteNotFound:
    pass


@dataclass(frozen=True)
class MyNameIs(Note):
    name: str


@dataclass(frozen=True)
class IAmPresident(Note):
    presidential_token: str


@dataclass(frozen=True)
class NewMemberAdded(Note):
    name: str


T = TypeVar('T')


class NoteFinder(ABC):
    @abstractmethod
    def find_notes(self, note_type: Type[T]) -> set[T]:
        """Find notes of a certain type"""

    @abstractmethod
    def find_one_note(self, note_type: Type[T]) -> T | NoteNotFound:
        """Find precisely one note of a certain type"""

    @abstractmethod
    def find_notes_of(self, actor: ActorName) -> NoteFinder:
        """View notes of certain actor"""


class NoteBookCollection(NoteFinder):
    def __init__(self):
        self._notebooks: dict[ActorName, NoteBook] = {}

    def add_notebook_for(self, actor_name: ActorName) -> NoteBook:
        note_book = NoteBook(actor_name)
        self._notebooks[actor_name] = note_book
        return note_book

    def find_notes_of(self, actor: ActorName) -> NoteBook:
        return self._notebooks[actor]

    def find_notes(self, note_type: Type[T]) -> set[T]:
        result = set()
        for note_book in self._notebooks.values():
            result |= note_book.find_notes(note_type)

        return result

    def find_one_note(self, note_type: Type[T]) -> T | NoteNotFound:
        notes = self.find_notes(note_type)
        if len(notes) == 1:
            return notes.pop()

        return NoteNotFound()


class NoteBook(NoteFinder):
    def __init__(self, owner: ActorName):
        self._notes = set()
        self._owner = owner

    def find_notes(self, note_type: Type[T]) -> set[T]:
        return {note for note in self._notes if isinstance(note, note_type)}

    def find_one_note(self, note_type: Type[T]) -> T | NoteNotFound:
        for note in self._notes:
            if isinstance(note, note_type):
                return note

        return NoteNotFound()

    def find_notes_of(self, actor: ActorName) -> NoteFinder:
        if actor == self._owner:
            return self

        return NoteBook(owner=actor)

    def write(self, note: Note) -> None:
        self._notes.add(note)
