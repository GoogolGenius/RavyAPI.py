from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient",)

import asyncio

from typing import Any

import aiohttp

from .const import BASE_URL
from .errors import HTTPException


class HTTPClient:
    def __init__(self, token: str, loop: asyncio.AbstractEventLoop) -> None:
        self._headers = {"Authorization": f"Ravy {token}"}
        self._session = aiohttp.ClientSession(loop=loop, headers=self._headers)

        if not token:
            raise ValueError("No API token provided")

    async def close(self) -> None:
        await self._session.close()

    async def _validate(self, response: aiohttp.ClientResponse) -> None:
        if not response.ok:
            raise HTTPException(response.status, await response.text())

    async def get(self, path: str) -> dict[Any, Any]:
        async with self._session.get(BASE_URL + path) as response:
            await self._validate(response)
            return await response.json()
