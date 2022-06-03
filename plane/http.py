from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient", "HTTPAwareEndpoint")

import aiohttp
import re

from typing import Any

from plane.api.errors import HTTPException
from plane.api.models import GetTokenResponse
from plane.api.paths import Paths
from plane.const import BASE_URL, KSOFT_TOKEN_REGEX, RAVY_TOKEN_REGEX


class HTTPClient:
    """The internal HTTP client for handling requests to the Ravy API."""

    def __init__(self, token: str) -> None:
        self._token: str = self._token_sentinel(token)
        self._permissions: list[str] | None = None
        self._phisherman_token: str | None = None
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(
            headers={"Authorization": token}
        )

    @staticmethod
    async def _handle_response(response: aiohttp.ClientResponse) -> None:
        if not response.ok:
            try:
                data = await response.json()
            except aiohttp.ContentTypeError:
                data = await response.text()

            raise HTTPException(response.status, data)

    @staticmethod
    def _token_sentinel(token: str) -> str:
        """Validate the current token.

        Returns
        -------
        Literal["Ravy", "KSoft"]
            The type of token.
        Raises
        ------
        ValueError
            If the token is invalid.
        """
        ravy = re.compile(RAVY_TOKEN_REGEX)
        ksoft = re.compile(KSOFT_TOKEN_REGEX)

        if not any(regex.match(token) for regex in (ravy, ksoft)):
            raise ValueError("Invalid token provided")

        return token

    async def _get_permissions(self) -> None:
        if self._permissions is not None:
            return

        async with self._session.get(BASE_URL + self.paths.tokens.route) as response:
            await self._handle_response(response)
            self._permissions = GetTokenResponse(await response.json()).access

    async def get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Execute a GET request to the Ravy API.

        Parameters
        ----------
        path : str
            The path URL to the route.
        params : dict[str, str] | None
            The query parameters to send with the request, if any.
        """
        await self._get_permissions()

        async with self._session.get(BASE_URL + path, params=params) as response:
            await self._handle_response(response)
            return await response.json()

    async def post(
        self,
        path: str,
        *,
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
        await self._get_permissions()

        async with self._session.post(
            BASE_URL + path, json=data, params=params
        ) as response:
            await self._handle_response(response)
            return await response.json()

    def set_phisherman_token(self, token: str) -> None:
        """Set the phisherman token.

        Parameters
        ----------
        token : str
            The phisherman token.
        """
        self._phisherman_token = token

    async def close(self) -> None:
        await self._session.close()

    @property
    def paths(self) -> Paths:
        """The route paths for the Ravy API."""
        return Paths()

    @property
    def permissions(self) -> list[str] | None:
        """The permissions for the current token."""
        return self._permissions

    @property
    def phisherman_token(self) -> str | None:
        """The phisherman token for the current token."""
        return self._phisherman_token


class HTTPAwareEndpoint:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http
