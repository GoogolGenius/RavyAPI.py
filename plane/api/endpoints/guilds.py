from __future__ import annotations

__all__: tuple[str, ...] = ("Guilds",)

from ...http import HTTPClient
from ..models import GetGuildResponse


class Guilds:
    """The implementation class for requests to the `guilds` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_guild(self, guild_id: int) -> GetGuildResponse:
        """Get extensive guild information.

        Parameters
        ----------
        guild_id : int
            Guild ID of the guild to look up.

        Returns
        -------
        GetGuildResponse
            The response from the API.
        """
        return GetGuildResponse(
            await self._http.get(self._http.paths.guilds(guild_id).route)
        )
