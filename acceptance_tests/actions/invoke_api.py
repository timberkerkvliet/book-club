from dataclasses import dataclass

from acceptance_tests.actions.get_invoker import get_invoker
from book_club.failure import Failure
from book_club.request_handler import request_handler
from pyplay.log_book import LogMessage


@dataclass(frozen=True)
class ExecutedCommand(LogMessage):
    success: bool


async def invoke_api(command, app, log_book, character_name):
    handler = request_handler(app.context)

    result = await handler.handle_command(
        invoker=get_invoker(log_book, character_name),
        command=command
    )

    log_book.write_message(ExecutedCommand(success=result != Failure()))

    return result
