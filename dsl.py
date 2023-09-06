from contextlib import asynccontextmanager, contextmanager
from typing import Self


class Interaction:
    pass


class Assertion:
    pass


class AddANewMember(Interaction):
    ...


class Play:
    def __init__(self):
        self._actors = []

    def with_actor_called(self, name: str) -> Actor:
        return Actor(self)

    async def execute(self) -> None:
        ...


class AccessPresidentialInterface:
    pass


class Actor:
    def __init__(self, play: Play):
        self._play = play
        self._abilities = []

    def who_can(self, *abilities) -> Self:
        self._abilities.extend(abilities)
        return self

    def performs(self, *interactions: Interaction):
        ...

    def expects(self, *assertions):
        ...


@asynccontextmanager
async def executable_play():
    play = Play()
    yield play
    await play.execute()
