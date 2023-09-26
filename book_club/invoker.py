from __future__ import annotations

import typing
from dataclasses import dataclass


@dataclass(frozen=True)
class President:
    pass


@dataclass(frozen=True)
class Member:
    name: str


@dataclass(frozen=True)
class Anonymous:
    pass


Invoker = typing.Union[President, Member, Anonymous]
