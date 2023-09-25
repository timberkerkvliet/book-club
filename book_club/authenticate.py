import os

from book_club.request_context import Invoker, Member, President


async def authenticate(token: str) -> Invoker:
    if token == os.getenv('PRESIDENTIAL_TOKEN', ''):
        return President()

    return Member()
