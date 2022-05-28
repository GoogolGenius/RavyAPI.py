from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

from ..http import HTTPClient
from ..models import GetGuildResponse


class URLs:
    """The implementation class for requests to the `urls` endpoint."""

    def __init__(self, http: HTTPClient) -> None:
        """
        Parameters
        ----------
        http : HTTPClient
            The internal HTTP client to use for requests.
        """
        self._http = http

    async def get_website(self, id: int) -> GetGuildResponse:
        """Analyze a URL by requesting the Ravy API.

        Parameters
        ----------
        id : int
            The Discord ID of the guild.
        """
        return GetGuildResponse(await self._http.get(self._http.paths.guilds(id).route))
