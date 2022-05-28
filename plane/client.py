from __future__ import annotations

__all__: tuple[str, ...] = ("Client",)

import asyncio

from .routes import Users, URLs, Tokens
from .http import HTTPClient


class Client:
    """The heart and soul of the client interface to the Ravy API.

    Attributes
    ----------
    token : str
        The token used to authenticate with the Ravy API.
    loop : asyncio.AbstractEventLoop
        The asyncio event loop used to run the client.

    Methods
    -------
    close()
        Close the client.
    """

    def __init__(self, token: str, loop: asyncio.AbstractEventLoop | None = None):
        """
        Parameters
        ----------
        token : str
            The token used to authenticate with the Ravy API.
        loop : asyncio.AbstractEventLoop
            The asyncio event loop used to run the client.

        Raises
        ------
        ValueError
            If no token is provided.
        """
        self.token = token
        self.loop = loop or asyncio.get_event_loop()
        self._http = HTTPClient(token, self.loop)
        self._closed: bool = False
        self._users = Users(self._http)
        self._urls = URLs(self._http)
        self._tokens = Tokens(self._http)

    async def close(self) -> None:
        """Close the client."""
        await self._http.close()
        self._closed = True

    @property
    def closed(self) -> bool:
        """Whether the client is closed."""
        return self._closed

    @property
    def users(self) -> Users:
        """The users endpoint."""
        return self._users

    @property
    def urls(self) -> URLs:
        """The urls endpoint."""
        return self._urls

    @property
    def tokens(self) -> Tokens:
        """The tokens endpoint."""
        return self._tokens
