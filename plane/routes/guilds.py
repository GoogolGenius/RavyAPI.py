from __future__ import annotations

__all__: tuple[str, ...] = ("Guilds",)

from ..http import HTTPClient
from ..models import GetGuildResponse


class Guilds:
    """The implementation class for requests to the `guilds` endpoint."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_guild(self, guild_id: int) -> GetGuildResponse:
        """Analyze a URL by requesting the Ravy API.

        Parameters
        ----------
        guild_id : int
            The Discord ID of the guild.
        """
        return GetGuildResponse(
            await self._http.get(self._http.paths.guilds(guild_id).route)
        )
