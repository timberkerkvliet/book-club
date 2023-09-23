import asyncio
from asyncio import Event

from book_club.app import app


async def run():
    async with app():
        await Event().wait()

asyncio.run(run())
