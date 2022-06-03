from __future__ import annotations

__all__: tuple[str, ...] = ("Client",)

from plane.http import HTTPClient
from plane.api.endpoints import Avatars, Guilds, KSoft, Users, URLs, Tokens


class Client:
    """The heart and soul of the client interface to the Ravy API.

    Attributes
    ----------
    token : str
        The token used to authenticate with the Ravy API.
    token_type : Literal["Ravy", "KSoft"]
        The type of token used to authenticate with the Ravy API.
    loop : asyncio.AbstractEventLoop | None
        The asyncio event loop used to run the client.
        Default event loop is used if None.

    Methods
    -------
    close()
        Close the client.
    """

    def __init__(self, token: str):
        """
        Parameters
        ----------
        token : str
            The token used to authenticate with the API.
        token_type : Literal["Ravy", "KSoft"]
            The type of token used to authenticate.
        loop : asyncio.AbstractEventLoop
            The asyncio event loop used to run the client.

        !!! note
            If `token_type` is "KSoft", only the `ksoft` endpoint is supported. All
            endpoints are available with "Ravy."There is no wrapper validation for this.
            Upon an invalid request, the generic `HTTPException` will be raised with
            the respective information.
        """
        self._token = token
        self._http = HTTPClient(self._token)
        self._closed: bool = False
        self._avatars = Avatars(self._http)
        self._guilds = Guilds(self._http)
        self._ksoft = KSoft(self._http)
        self._users = Users(self._http)
        self._urls = URLs(self._http)
        self._tokens = Tokens(self._http)

    async def close(self) -> None:
        """Close the client."""
        await self._http.close()
        self._closed = True

    def set_phisherman_token(self, token: str) -> Client:
        """Set the phisherman token.

        Parameters
        ----------
        token : str
            The phisherman token to use for `urls` routes.
        """
        self._http.set_phisherman_token(token)

        return self  # for future chaining

    @property
    def closed(self) -> bool:
        """Whether the client is closed."""
        return self._closed

    @property
    async def avatars(self) -> Avatars:
        """The avatars endpoint."""
        return self._avatars

    @property
    def guilds(self) -> Guilds:
        """The guilds endpoint."""
        return self._guilds

    @property
    def ksoft(self) -> KSoft:
        """The ksoft endpoint."""
        return self._ksoft

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
