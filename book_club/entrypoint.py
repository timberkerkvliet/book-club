import asyncio
import signal
from asyncio import Event

from book_club.app import app


async def run():
    async with app():
        event = Event()
        signal.signal(signal.SIGTERM, event.set)
        await event.wait()

asyncio.run(run())
