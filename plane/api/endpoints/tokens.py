from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)

from typing import TYPE_CHECKING

from ..models import GetTokenResponse

if TYPE_CHECKING:
    from ...http import HTTPClient


class Tokens:
    """The implementation class for requests to the `tokens` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_token(self) -> GetTokenResponse:
        """Get current token information.

        Returns
        -------
        GetTokenResponse
            The response from the API.
        """
        return GetTokenResponse(await self._http.get(self._http.paths.tokens.route))
