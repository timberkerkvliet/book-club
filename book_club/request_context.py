from __future__ import annotations

import typing
from contextlib import AsyncExitStack
from dataclasses import dataclass

from book_club.app_context import AppContext


@dataclass
class President:
    pass


class Member:
    pass


Invoker = typing.Union[President, Member]


class RequestContext:
    def __init__(self, app_context: AppContext, invoker: Invoker):
        self._app_context = app_context
        self._invoker = invoker

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

    async def join(self, context_manager):
        return await self._exit_stack.enter_async_context(context_manager)


T = typing.TypeVar('T')


class RequestResource(typing.Generic[T]):
    def __init__(self, f: typing.Callable[[RequestContext], typing.AsyncGenerator[T]]):
        self._f = f
        self._generator = None
        self._created = False

    async def __aenter__(self):
        return

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return

    async def __call__(self, app_context: RequestContext) -> T:
        if not self._created:
            self._generator = self._f(app_context)
            self._resource = await self._generator.__anext__()
            self._created = True

        return self._resource


def request_resource(f: typing.Callable[[RequestContext], typing.AsyncGenerator[T]]) -> RequestResource[T]:
    return RequestResource(f)
