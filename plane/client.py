from __future__ import annotations

__all__: tuple[str, ...] = ("Client",)

import asyncio

from plane.endpoints.users import Users
from plane.endpoints.urls import URLs

from .http import HTTPClient
from .routes import Routes


class Client:
    def __init__(self, api_key: str, loop: asyncio.AbstractEventLoop | None = None):
        self._loop = loop or asyncio.get_event_loop()
        self._http = HTTPClient(api_key, self._loop)
        self._routes = Routes()

        self._users = Users(self._http, self._routes)
        self._urls = URLs(self._http, self._routes)

    @property
    def users(self) -> Users:
        return self._users
    
    @property
    def urls(self) -> URLs:
        return self._urls

    async def close(self):
        await self._http.close()
