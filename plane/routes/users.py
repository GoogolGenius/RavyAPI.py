from __future__ import annotations

__all__: tuple[str, ...] = ("Users",)

from ..http import HTTPClient
from ..models import (
    GetUserResponse,
    GetPronounsResponse,
    GetBansResponse,
    GetWhitelistsResponse,
    GetReputationResponse,
)


class Users:
    """The implementation class for requests to the `users` endpoint."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_user(self, id: int) -> GetUserResponse:
        """Fetch a user from the Ravy API.

        Parameters
        ----------
        id : int
            The user's Discord ID.

        Returns
        -------
        GetUserResponse
            The user's information model.
        """
        return GetUserResponse(await self._http.get(self._http.paths.users.user(id)))

    async def get_pronouns(self, id: int) -> GetPronounsResponse:
        """Fetch a user's pronouns from the Ravy API.

        Parameters
        ----------
        id : int
            The user's Discord ID.

        Returns
        -------
        GetPronounsResponse
            The user's pronouns model.
        """
        return GetPronounsResponse(
            await self._http.get(self._http.paths.users.pronouns(id))
        )

    async def get_bans(self, id: int) -> GetBansResponse:
        """Fetch a user's bans from the Ravy API.

        Parameters
        ----------
        id : int
            The user's Discord ID.

        Returns
        -------
        GetBansResponse
            The user's bans model.
        """
        return GetBansResponse(await self._http.get(self._http.paths.users.bans(id)))

    async def get_whitelists(self, id: int) -> GetWhitelistsResponse:
        """Fetch a user's whitelists from the Ravy API.

        Parameters
        ----------
        id : int
            The user's Discord ID.

        Returns
        -------
        GetWhitelistsResponse
            The user's whitelists model.
        """
        return GetWhitelistsResponse(
            await self._http.get(self._http.paths.users.whitelists(id))
        )

    async def get_reputation(self, id: int) -> GetReputationResponse:
        """Fetch a user's reputation from the Ravy API.

        Parameters
        ----------
        id : int
            The user's Discord ID.

        Returns
        -------
        GetReputationResponse
            The user's reputation model.
        """
        return GetReputationResponse(
            await self._http.get(self._http.paths.users.reputation(id))
        )
