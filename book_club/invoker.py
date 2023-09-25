from __future__ import annotations

import typing
from dataclasses import dataclass


@dataclass
class President:
    pass


@dataclass
class Member:
    name: str


Invoker = typing.Union[President, Member]
