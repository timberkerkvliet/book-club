from contextlib import asynccontextmanager
from typing import Any, Type

from book_club.app_context import AppContext
from book_club.request_context import RequestContext


class RequestHandler:
    def __init__(
        self,
        command_handlers: dict,
        query_handlers: dict,
        app_context: AppContext
    ):
        self._command_handlers = command_handlers
        self._query_handlers = query_handlers
        self._app_context = app_context

    @property
    def command_types(self) -> set[Type]:
        return set(self._command_handlers.keys())

    @asynccontextmanager
    async def _request_context(self, invoker):
        context = RequestContext(
            app_context=self._app_context,
            invoker=invoker
        )
        async with context:
            yield context

    async def handle_command(
        self,
        invoker,
        command
    ) -> Any:
        coro = self._command_handlers[type(command)]
        async with self._request_context(invoker) as context:
            return await coro(command, context)

    async def handle_query(
        self,
        invoker,
        query
    ) -> Any:
        coro = self._query_handlers[type(query)]
        async with self._request_context(invoker) as context:
            return await coro(query, context)
