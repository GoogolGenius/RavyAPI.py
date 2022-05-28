from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)


from ..http import HTTPClient
from ..models import GetTokenResponse


class Tokens:
    """The implementation class for requests to the `tokens` endpoint."""

    def __init__(self, http: HTTPClient) -> None:
        """
        Parameters
        ----------
        http : HTTPClient
            The internal HTTP client to use for requests.
        """
        self._http = http

    async def get_token(self) -> GetTokenResponse:
        """Fetch the current token from the Ravy API."""
        return GetTokenResponse(await self._http.get(self._http.paths.tokens(self._http.token).route))
