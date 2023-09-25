from __future__ import annotations

from contextlib import AsyncExitStack
from typing import AsyncGenerator, Callable, AsyncContextManager, TypeVar, Generic


class AppContext:
    def __init__(self, is_fake: bool):
        self._is_fake = is_fake

    def is_fake(self) -> bool:
        return self._is_fake

    async def __aenter__(self) -> AppContext:
        self._exit_stack = AsyncExitStack()
        await self._exit_stack.__aenter__()

        return self

    async def __aexit__(self, *exc):
        await self._exit_stack.__aexit__(*exc)

    async def join(self, context_manager):
        return await self._exit_stack.enter_async_context(context_manager)


T = TypeVar('T')


class AppResource(Generic[T]):
    def __init__(self, f: Callable[[AppContext], AsyncGenerator[T]]):
        self._f = f
        self._generator = None
        self._created = False

    async def __aenter__(self):
        return

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return

    async def __call__(self, app_context: AppContext) -> T:
        if not self._created:
            self._generator = self._f(app_context)
            self._resource = await self._generator.__anext__()
            self._created = True

        return self._resource


def app_resource(f: Callable[[AppContext], AsyncGenerator[T]]) -> AppResource[T]:
    return AppResource(f)
