from __future__ import annotations

__all__: tuple[str, ...] = ("Client",)

import asyncio

from typing import Optional

from .endpoints import Users
from .endpoints import URLs

from .http import HTTPClient
from .routes import Routes


class Client:
    _ROUTES = Routes()

    def __init__(self, token: str, loop: Optional[asyncio.AbstractEventLoop] = None):
        self.loop = loop or asyncio.get_event_loop()
        self._http = HTTPClient(token, self.loop)
        self._closed: bool = False
        self._users = Users(self._http, self._ROUTES)
        self._urls = URLs(self._http, self._ROUTES)

    async def close(self) -> None:
        await self._http.close()
        self._closed = True

    @property
    def closed(self) -> bool:
        return self._closed

    @property
    def users(self) -> Users:
        return self._users

    @property
    def urls(self) -> URLs:
        return self._urls
