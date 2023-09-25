from typing import AsyncGenerator

from aiohttp import ClientSession

from book_club.app_context import app_resource, AppContext


@app_resource
async def app_http_session(app_context: AppContext) -> AsyncGenerator[ClientSession, None]:
    async with ClientSession() as session:
        yield session
