from functools import lru_cache
from typing import Type

from book_club.adapter_type import AppContext
from book_club.add_a_new_member import AddNewMember, add_a_new_member


class RequestHandler:
    def __init__(self, command_handlers: dict, app_context: AppContext):
        self._command_handlers = command_handlers
        self._app_context = app_context

    @property
    def command_types(self) -> set[Type]:
        return set(self._command_handlers.keys())

    async def handle_command(self, command) -> None:
        coro = self._command_handlers[type(command)]
        return await coro(command, self._app_context)


@lru_cache
def request_handler(app_context: AppContext) -> RequestHandler:
    return RequestHandler(
        command_handlers={
            AddNewMember: add_a_new_member
        },
        app_context=app_context
    )
