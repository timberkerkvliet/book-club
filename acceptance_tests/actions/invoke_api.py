from acceptance_tests.actions.get_invoker import get_invoker
from book_club.failure import Failure
from book_club.request_handler import request_handler
from pyplay.action_executor import FailedAction
from pyplay.log_book import LogMessage


class FailedCommand(LogMessage):
    pass


async def invoke_api(command, app, log_book, character_name):
    handler = request_handler(app.context)

    result = await handler.handle_command(
        invoker=get_invoker(log_book, character_name),
        command=command
    )

    if result == Failure():
        log_book.write_message(FailedCommand())
        return FailedAction()
