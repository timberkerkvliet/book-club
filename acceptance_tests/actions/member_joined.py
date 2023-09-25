from __future__ import annotations

from dataclasses import dataclass

from pyplay.log_book import LogMessage


@dataclass(frozen=True)
class MemberJoined(LogMessage):
    member_name: str
