from __future__ import annotations

from contextlib import AsyncExitStack, asynccontextmanager
from typing import Any, AsyncGenerator, Callable, AsyncContextManager, TypeVar, Generic


class AppContext:
    def __init__(self, is_fake: bool):
        self._is_fake = is_fake
        self._resources: dict[int, Any] = {}

    def is_fake(self) -> bool:
        return self._is_fake

    async def __aenter__(self) -> AppContext:
        self._exit_stack = AsyncExitStack()
        await self._exit_stack.__aenter__()

        return self

    async def __aexit__(self, *exc):
        await self._exit_stack.__aexit__(*exc)

    async def get_resource(
        self,
        resource_id: int,
        context_manager: Callable[[AppContext], AsyncContextManager]
    ):
        if resource_id not in self._resources:
            self._resources[resource_id] = await self._exit_stack.enter_async_context(context_manager(self))

        return self._resources[resource_id]


T = TypeVar('T')


class AppResource(Generic[T]):
    def __init__(self, context_manager: Callable[[AppContext], AsyncContextManager[T]]):
        self._context_manager = context_manager
        self._id = id(self._context_manager)

    async def __call__(self, app_context: AppContext) -> T:
        return await app_context.get_resource(
            resource_id=self._id,
            context_manager=self._context_manager
        )


def app_resource(f: Callable[[AppContext], AsyncGenerator[T]]) -> AppResource[T]:
    return AppResource(asynccontextmanager(f))
