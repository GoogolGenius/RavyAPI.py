# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("Client",)

from plane.http import HTTPClient
from plane.api.endpoints import Avatars, Guilds, KSoft, URLs, Users, Tokens


class Client:
    """The client interface for interacting with the Ravy API.

    Attributes
    ----------
    closed : bool
        Whether or not the client is closed.
    avatars : Avatars
        The `avatars` endpoint.
    guilds : Guilds
        The `guilds` endpoint.
    ksoft : KSoft
        The `ksoft` endpoint.
    users : Users
        The `users` endpoint.
    urls : URLs
        The `urls` endpoint.
    tokens : Tokens
        The `tokens` endpoint.

    Methods
    -------
    close() -> None
        Closes the client, shutting down the underlying HTTP client.
    set_phisherman_token(token: str) -> Client
        Sets the phisherman token for the client.
    """

    __slots__: tuple[str, ...] = (
        "_token",
        "_http",
        "_closed",
        "_avatars",
        "_guilds",
        "_ksoft",
        "_users",
        "_urls",
        "_tokens",
    )

    def __init__(self, token: str) -> None:
        """
        Parameters
        ----------
        token : str
            The token used to authenticate with the API.
        """
        self._token: str = token
        self._http: HTTPClient = HTTPClient(self._token)
        self._closed: bool = False
        self._avatars: Avatars = Avatars(self._http)
        self._guilds: Guilds = Guilds(self._http)
        self._ksoft: KSoft = KSoft(self._http)
        self._users: Users = Users(self._http)
        self._urls: URLs = URLs(self._http)
        self._tokens: Tokens = Tokens(self._http)

    async def close(self) -> None:
        """Closes the client, shutting down the underlying HTTP client."""
        await self._http.close()
        self._closed = True

    def set_phisherman_token(self, token: str) -> Client:
        """Sets the phisherman token for the client.

        Parameters
        ----------
        token : str
            The phisherman token to set.

        Returns
        -------
        Client
            The client with the phisherman token set.
        """
        self._http.set_phisherman_token(token)
        return self

    @property
    def closed(self) -> bool:
        """Whether or not the client is closed."""
        return self._closed

    @property
    def avatars(self) -> Avatars:
        """The `avatars` endpoint."""
        return self._avatars

    @property
    def guilds(self) -> Guilds:
        """The `guilds` endpoint."""
        return self._guilds

    @property
    def ksoft(self) -> KSoft:
        """The `ksoft` endpoint."""
        return self._ksoft

    @property
    def users(self) -> Users:
        """The `users` endpoint."""
        return self._users

    @property
    def urls(self) -> URLs:
        """The `urls` endpoint."""
        return self._urls

    @property
    def tokens(self) -> Tokens:
        """The `tokens` endpoint."""
        return self._tokens
