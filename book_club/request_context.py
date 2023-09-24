from __future__ import annotations

from contextlib import AsyncExitStack

from book_club.app_context import AppContext
from book_club.member import Member


class President:
    pass


class RequestContext:
    def __init__(self, app_context: AppContext, invoker: President | Member):
        self._app_context = app_context
        self._invoker = invoker

    @property
    def app_context(self) -> AppContext:
        return self._app_context

    @property
    def invoker(self) -> President | Member:
        return self._invoker

    async def __aenter__(self) -> RequestContext:
        self._exit_stack = AsyncExitStack()
        await self._exit_stack.__aenter__()

        return self

    async def __aexit__(self, *exc):
        await self._exit_stack.__aexit__(*exc)

    async def join(self, context_manager):
        return await self._exit_stack.enter_async_context(context_manager)
