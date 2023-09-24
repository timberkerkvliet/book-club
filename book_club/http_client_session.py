from typing import AsyncContextManager

from aiohttp import ClientSession

from book_club.app_context import app_resource, AppContext


@app_resource
def app_http_session(app_context: AppContext) -> AsyncContextManager[ClientSession]:
    return ClientSession()
