from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)

from plane.api.models import GetTokenResponse
from plane.http import HTTPAwareEndpoint


class Tokens(HTTPAwareEndpoint):
    """The implementation class for requests to the `tokens` route."""

    async def get_token(self: HTTPAwareEndpoint) -> GetTokenResponse:
        """Get current token information.

        Returns
        -------
        GetTokenResponse
            The response from the API.
        """
        return GetTokenResponse(await self._http.get(self._http.paths.tokens.route))
