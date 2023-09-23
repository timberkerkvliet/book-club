from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class AppContext:
    id: UUID
    is_fake: bool
