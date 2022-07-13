# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Internal HTTP objects to create requests and handle responses."""

from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPClient", "HTTPAwareEndpoint")

import logging
import re
from typing import Any

import aiohttp
from typing_extensions import Final

from plane.api.errors import (
    BadRequestError,
    ForbiddenError,
    HTTPError,
    NotFoundError,
    TooManyRequestsError,
    UnauthorizedError,
)
from plane.api.models import GetTokenResponse
from plane.api.paths import Paths
from plane.const import BASE_URL, KSOFT_TOKEN_REGEX, RAVY_TOKEN_REGEX, USER_AGENT

_LOGGER: Final[logging.Logger] = logging.getLogger("plane.http")


class HTTPClient:
    """Internal client using aiohttp to work with networking."""

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
        HTTPError
            If the response is not an acceptable status code.
        """
        if response.ok:
            _LOGGER.debug("Handling response successfully: %s", response.status)
            return

        try:
            data: str | dict[str, Any] = await response.json()
            _LOGGER.debug("Response type is of JSON; returning as %s", type(data))
        except aiohttp.ContentTypeError:
            data = await response.text()  # errors are not always JSON
            _LOGGER.debug("Response type is not of JSON; returning as %s", type(data))

        _LOGGER.critical("Response status is not ok: %s", response.status)

        exception_map = {
            400: BadRequestError,
            401: UnauthorizedError,
            403: ForbiddenError,
            404: NotFoundError,
            429: TooManyRequestsError,
        }

        if response.status in exception_map:
            raise exception_map[response.status](data)
        else:
            raise HTTPError(response.status, data)

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
            _LOGGER.critical("An error occurred while validating token")
            raise ValueError("Invalid token provided")

        _LOGGER.debug("Token is successfully validated")
        return token

    async def get_permissions(self) -> None:
        """Get the permissions for the current token."""
        _LOGGER.debug("Getting permissions from token")

        if self._permissions is not None:
            _LOGGER.debug("Permissions already set; skipping API call")
            return

        self._permissions = GetTokenResponse(await self.get(self.paths.tokens.route)).access

        _LOGGER.debug("Permissions are now set: %s", self.permissions)

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
        _LOGGER.debug("Making GET request to %s", path)
        async with self._session.get(BASE_URL + path, **kwargs) as response:
            await self._handle_response(response)

            data: dict[str, Any] = await response.json()
            return data

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
        _LOGGER.debug("Making POST request to %s", path)
        async with self._session.post(BASE_URL + path, **kwargs) as response:
            await self._handle_response(response)

            data: dict[str, Any] = await response.json()
            return data

    def set_phisherman_token(self, token: str) -> None:
        """Set the phisherman token for use in `urls` endpoint routes."""
        self._phisherman_token = token

    async def close(self) -> None:
        """Close the underlying aiohttp client."""
        _LOGGER.debug("Closing underlying aiohttp client")
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
        Should be populated with a list of string permissions after an initial request
        that is known to require validatation.
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
        self._http: HTTPClient = http
