from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient",)

import asyncio

from typing import Any

import aiohttp

from .errors import HTTPException
from .routes.paths import Paths


class HTTPClient:
    """The internal HTTP client for handling requests to the Ravy API."""

    def __init__(self, token: str, loop: asyncio.AbstractEventLoop) -> None:
        self._headers: dict[str, str] = {"Authorization": f"Ravy {token}"}
        self._session = aiohttp.ClientSession(loop=loop, headers=self._headers)

        if not token:
            raise ValueError("No API token provided")

    async def close(self) -> None:
        await self._session.close()

    async def _validate(self, response: aiohttp.ClientResponse) -> None:
        if not response.ok:
            raise HTTPException(response.status, await response.text())

    async def get(self, path: str) -> dict[str, Any]:
        """Execute a GET request to the Ravy API.

        Parameters
        ----------
        path : str
            The path URL to the endpoint.
        """
        async with self._session.get(self.paths.base + path) as response:
            await self._validate(response)
            return await response.json()

    async def post(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        """Execute a POST request to the Ravy API.

        Parameters
        ----------
        path : str
            The path URL to the endpoint.
        data : dict[str, Any]
            The JSON data to send with the request.
        """
        async with self._session.post(self.paths.base + path, json=data) as response:
            await self._validate(response)
            return await response.json()

    @property
    def paths(self) -> Paths:
        """The URL paths for the Ravy API."""
        return Paths()
