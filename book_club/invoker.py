from __future__ import annotations

import typing
from dataclasses import dataclass


@dataclass
class President:
    pass


@dataclass
class Member:
    name: str


@dataclass
class Anonymous:
    pass


Invoker = typing.Union[President, Member, Anonymous]
