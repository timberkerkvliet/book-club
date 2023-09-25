import os

from book_club.invoker import President, Member, Invoker


async def authenticate(token: str) -> Invoker:
    if token == os.getenv('PRESIDENTIAL_TOKEN', ''):
        return President()

    return Member()
