from typing import Type

from book_club.add_a_new_member import AddNewMemberCommand, add_a_new_member


class RequestHandler:
    def __init__(self, command_handlers: dict):
        self._command_handlers = command_handlers

    @property
    def command_types(self) -> set[Type]:
        return set(self._command_handlers.keys())

    async def handle_command(self, command) -> None:
        coro = self._command_handlers[type(command)]
        return await coro(command)


def request_handler() -> RequestHandler:
    return RequestHandler(
        command_handlers={
            AddNewMemberCommand: add_a_new_member
        }
    )
