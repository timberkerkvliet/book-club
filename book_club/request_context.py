from __future__ import annotations

import typing
from typing import Callable
from contextlib import AsyncExitStack

from book_club.app_context import AppContext
from book_club.invoker import Invoker


class RequestContext:
    def __init__(self, app_context: AppContext, invoker: Invoker):
        self._app_context = app_context
        self._invoker = invoker
        self._resources: dict[int, typing.Any] = {}

    @property
    def app_context(self) -> AppContext:
        return self._app_context

    @property
    def invoker(self) -> Invoker:
        return self._invoker

    async def __aenter__(self) -> RequestContext:
        self._exit_stack = AsyncExitStack()
        await self._exit_stack.__aenter__()

        return self

    async def __aexit__(self, *exc):
        await self._exit_stack.__aexit__(*exc)

    async def get_resource(
        self,
        resource_id: int,
        context_manager: Callable[[RequestContext], typing.AsyncContextManager]
    ):
        if resource_id not in self._resources:
            self._resources[resource_id] = await self._exit_stack.enter_async_context(context_manager(self))

        return self._resources[resource_id]


T = typing.TypeVar('T')


class RequestResource(typing.Generic[T]):
    def __init__(self, context_manager: typing.Callable[[RequestContext], typing.AsyncContextManager[T]]):
        self._context_manager = context_manager
        self._id = id(context_manager)

    async def __call__(self, request_context: RequestContext) -> T:
        return await request_context.get_resource(
            resource_id=self._id,
            context_manager=self._context_manager
        )


def request_resource(f: typing.Callable[[RequestContext], typing.AsyncContextManager[T]]) -> RequestResource[T]:
    return RequestResource(f)
