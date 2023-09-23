from dataclasses import dataclass
from uuid import UUID

from book_club.app_context import AppContext


@dataclass(frozen=True)
class RequestContext:
    id: UUID
    app_context: AppContext
