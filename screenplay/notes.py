from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Tuple, Type, TypeVar

from screenplay.actor_name import ActorName


T = TypeVar('T')


class Note:
    pass


@dataclass(frozen=True)
class NoteRecord(Generic[T]):
    author: ActorName
    note: T


class NoteFinder(ABC):
    @abstractmethod
    def find_note_type(self, note_type: Type[T]) -> NoteFinder:
        """Find notes of a certain type"""

    @abstractmethod
    def one(self) -> Note:
        """Find precisely one note of a certain type"""

    @abstractmethod
    def find_notes_of(self, actor: ActorName) -> NoteFinder:
        """View notes of certain actor"""


class NoteWriter(ABC):
    def __init__(self, author: ActorName, collection: NoteRecords):
        self._author = author
        self._collection = collection

    def write(self, note: Note) -> None:
        self._collection.add(
            NoteRecord(
                author=self._author,
                note=note
            )
        )


class NoteRecords(NoteFinder):
    def __init__(self, records: list[NoteRecord] = None):
        self._records = records or []

    def find_note_type(self, note_type: Type[T]) -> NoteRecords:
        return NoteRecords(
            [
                note_record for note_record in self._records
                if isinstance(note_record.note, note_type)
            ]
        )

    def one(self) -> T:
        if len(self._records) == 1:
            return self._records[0].note

        raise Exception

    def find_notes_of(self, actor: ActorName) -> NoteFinder:
        return NoteRecords(
            [
                note_record
                for note_record in self._records
                if note_record.author == actor
            ]
        )

    def add(self, record: NoteRecord) -> NoteRecords:
        self._records.append(record)
        return self

    def get_writer_for(self, actor: ActorName) -> NoteWriter:
        return NoteWriter(
            author=actor,
            collection=self
        )
