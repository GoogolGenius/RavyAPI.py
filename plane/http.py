from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient",)

import asyncio

from typing import Any
from typing_extensions import Literal

import aiohttp

from .const import BASE_URL
from .api.errors import HTTPException
from .api.paths import Paths


class HTTPClient:
    """The internal HTTP client for handling requests to the Ravy API."""

    def __init__(
        self,
        token: str,
        token_type: Literal["Ravy", "KSoft"],
        loop: asyncio.AbstractEventLoop,
    ) -> None:
        self._session = aiohttp.ClientSession(
            loop=loop, headers={"Authorization": f"{token_type} {token}"}
        )

    async def close(self) -> None:
        await self._session.close()

    @staticmethod
    async def _handle(response: aiohttp.ClientResponse) -> None:
        if not response.ok:
            try:
                data = await response.json()
            except aiohttp.ContentTypeError:
                data = await response.text()

            raise HTTPException(response.status, data)

    async def get(
        self, path: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Execute a GET request to the Ravy API.

        Parameters
        ----------
        path : str
            The path URL to the route.
        params : dict[str, str] | None
            The query parameters to send with the request, if any.
        """
        async with self._session.get(
            BASE_URL + path, params=params
        ) as response:
            await self._handle(response)
            return await response.json()

    async def post(
        self,
        path: str,
        data: dict[str, Any],
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a POST request to the Ravy API.

        Parameters
        ----------
        path : str
            The path URL to the route.
        data : dict[str, Any]
            The JSON data to send with the request.
        """
        async with self._session.post(
            BASE_URL + path, json=data, params=params
        ) as response:
            await self._handle(response)
            return await response.json()

    @property
    def paths(self) -> Paths:
        """The route paths for the Ravy API."""
        return Paths()
