from functools import lru_cache
from typing import Any, Type

from book_club.app_context import AppContext

from book_club.current_read.declare_new_read import DeclareNewRead, declare_current_book
from book_club.member_list.join_club import JoinClub, join_club
from book_club.member_list.get_member_list import GetMemberList, get_member_list
from book_club.member_list.leave_club import LeaveClub, leave_club
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


def command_handlers():
    return {
        JoinClub: join_club,
        LeaveClub: leave_club,
        DeclareNewRead: declare_current_book
    }


def query_handlers():
    return {
        GetMemberList: get_member_list
    }


@lru_cache
def request_handler(app_context: AppContext) -> RequestHandler:
    return RequestHandler(
        command_handlers=command_handlers(),
        query_handlers=query_handlers(),
        app_context=app_context
    )
