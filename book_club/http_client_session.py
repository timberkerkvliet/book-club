from contextlib import asynccontextmanager

from aiohttp import ClientSession

from book_club.app_context import app_resource, AppContext


@app_resource
@asynccontextmanager
async def app_http_session(app_context: AppContext):
    async with aiohttp.ClientSession() as session:
        yield session