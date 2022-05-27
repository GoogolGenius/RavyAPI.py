from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient",)

import asyncio

from typing import Any

import aiohttp

from .errors import HTTPException


class HTTPClient:
    BASE_URL = "https://ravy.org/api/v1"

    def __init__(self, api_key: str, loop: asyncio.AbstractEventLoop) -> None:
        self._headers = {"Authorization": f"Ravy {api_key}"}
        self._session = aiohttp.ClientSession(loop=loop, headers=self._headers)

    async def _validate_response(self, response: aiohttp.ClientResponse) -> None:
        if not response.ok:
            raise HTTPException(response.status, await response.text())

    async def close(self) -> None:
        await self._session.close()

    async def get(self, path: str) -> dict[Any, Any]:
        async with self._session.get(self.BASE_URL + path) as response:
            print(self.BASE_URL + path)
            await self._validate_response(response)
            return await response.json()
