import signal
from asyncio import Event

from book_club.app_context import AppContext

from book_club.starlette import starlette_resource


class App:
    def __init__(self, fake_adapters: bool = False):
        self._context = AppContext(is_fake=fake_adapters)

    @property
    def context(self) -> AppContext:
        return self._context

    async def run(self) -> None:
        async with self._context:
            if not self._context.is_fake():
                await starlette_resource(self._context)

            event = Event()
            signal.signal(signal.SIGTERM, event.set)
            await event.wait()
