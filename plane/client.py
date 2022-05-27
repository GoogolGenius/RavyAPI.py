from __future__ import annotations

__all__: tuple[str, ...] = ("Client",)

import asyncio

from types import TracebackType
from typing import Optional

from .endpoints import Users
from .endpoints import URLs

from .http import HTTPClient
from .routes import Routes


class Client:
    _ROUTES = Routes()

    def __init__(self, token: str, loop: Optional[asyncio.AbstractEventLoop] = None):
        self._loop = loop or asyncio.get_event_loop()
        self._http = HTTPClient(token, self._loop)
        self._closed: bool = False

        self._users = Users(self._http, self._ROUTES)
        self._urls = URLs(self._http, self._ROUTES)

    async def __aenter__(self) -> Client:
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if not self._closed:
            await self.close()

    async def close(self) -> None:
        await self._http.close()
        self._closed = True

    @property
    def users(self) -> Users:
        return self._users

    @property
    def urls(self) -> URLs:
        return self._urls
