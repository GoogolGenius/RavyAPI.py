# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""Internal HTTP objects to create requests and handle responses."""

from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient", "HTTPAwareEndpoint")

import re

from typing import Any

import aiohttp

from plane.api.errors import HTTPException
from plane.api.models import GetTokenResponse
from plane.api.paths import Paths
from plane.const import BASE_URL, KSOFT_TOKEN_REGEX, RAVY_TOKEN_REGEX, USER_AGENT


class HTTPClient:
    """Internal client using aiohttp to work with networking.

    Methods
    -------
    get(path: str, **kwargs: Any) -> dict[str, Any]
        Make a GET request to the given path.
    post(path: str, **kwargs: Any) -> dict[str, Any]
        Make a POST request to the given path.
    close() -> None
        Close the underlying aiohttp client.
    """

    __slots__: tuple[str, ...] = (
        "_token",
        "_permissions",
        "_phisherman_token",
        "_headers",
        "_session",
    )

    def __init__(self, token: str) -> None:
        self._token: str = self._token_sentinel(token)
        self._permissions: list[str] | None = None
        self._phisherman_token: str | None = None
        self._headers: dict[str, str] = {
            "Authorization": token,
            "User-Agent": USER_AGENT,
        }
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(
            headers=self._headers
        )

    @staticmethod
    async def _handle_response(response: aiohttp.ClientResponse) -> None:
        """Process response errors for requests.

        Parameters
        ----------
        response : aiohttp.ClientResponse
            The response to process from the API.

        Raises
        ------
        HTTPException
            If the response is not a 200 status code.
        """
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
        token : str
            The token passed in to the client.

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
        """Get the permissions for the current token."""
        if self._permissions is not None:
            return

        async with self._session.get(BASE_URL + self.paths.tokens.route) as response:
            await self._handle_response(response)
            self._permissions = GetTokenResponse(await response.json()).access

    async def get(self, path: str, **kwargs: Any) -> dict[str, Any]:
        """Internal method to make a GET request to the given path.

        Parameters
        ----------
        path : str
            The path to make the request to.
        **kwargs : Any
            The keyword arguments to pass to aiohttp.

        Returns
        -------
        dict[str, Any]
            The JSON response from the API.
        """
        await self._get_permissions()

        async with self._session.get(BASE_URL + path, **kwargs) as response:
            await self._handle_response(response)
            return await response.json()

    async def post(self, path: str, **kwargs: Any) -> dict[str, Any]:
        """Internal method to make a POST request to the given path.

        Parameters
        ----------
        path : str
            The path to make the request to.
        **kwargs : Any
            The keyword arguments to pass to aiohttp.

        Returns
        -------
        dict[str, Any]
            The JSON response from the API.
        """
        await self._get_permissions()

        async with self._session.post(BASE_URL + path, **kwargs) as response:
            await self._handle_response(response)
            return await response.json()

    def set_phisherman_token(self, token: str) -> None:
        """Set the phisherman token for use in `urls` endpoint routes."""
        self._phisherman_token = token

    async def close(self) -> None:
        """Close the underlying aiohttp client."""
        await self._session.close()

    @property
    def headers(self) -> dict[str, str]:
        """The headers set in the aiohttp client for requests."""
        return self._headers

    @property
    def paths(self) -> Paths:
        """An instance of `plane.api.paths.Path` for routing."""
        return Paths()

    @property
    def permissions(self) -> list[str] | None:
        """The current permissions for the token.

        This is `None` if the token has not yet been retrieved.
        Should be populated with a list of string permissions after an initial request.
        """
        return self._permissions

    @property
    def phisherman_token(self) -> str | None:
        """The phisherman token for use in `urls` endpoint routes."""
        return self._phisherman_token


class HTTPAwareEndpoint:
    """A class representing an endpoint implementation aware of the underlying `plane.http.HTTPClient`."""

    __slots__: tuple[str, ...] = ("_http",)

    def __init__(self, http: HTTPClient) -> None:
        self._http = http
