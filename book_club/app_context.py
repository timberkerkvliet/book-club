from contextlib import AsyncExitStack
from dataclasses import dataclass
from typing import Callable, AsyncContextManager, TypeVar, Generic
from uuid import UUID


@dataclass(frozen=True)
class AppContext:
    id: UUID
    is_fake: bool
    exit_stack: AsyncExitStack


T = TypeVar('T')


class AppResource(Generic[T]):
    def __init__(self, f: Callable[[AppContext], AsyncContextManager[T]]):
        self._f = f
        self._resource = None

    async def __call__(self, app_context: AppContext) -> T:
        if self._resource is None:
            self._resource = app_context.exit_stack.enter_async_context(self._f(app_context))

        return self._resource


def app_resource(f):
    return AppResource(f)
