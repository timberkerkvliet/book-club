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

    def _request_context(self, invoker):
        return RequestContext(
            app_context=self._app_context,
            invoker=invoker
        )

    async def handle_command(
        self,
        invoker,
        command
    ) -> Any:
        coro = self._command_handlers[type(command)]
        return await coro(command, self._request_context(invoker))

    async def handle_query(
        self,
        invoker,
        query
    ) -> Any:
        coro = self._query_handlers[type(query)]
        return await coro(query, self._request_context(invoker))
