from __future__ import annotations

__all__: tuple[str, ...] = ("Users",)

from ...http import HTTPClient
from ..models import (
    GetUserResponse,
    GetPronounsResponse,
    GetBansResponse,
    GetWhitelistsResponse,
    GetReputationResponse,
)


class Users:
    """The implementation class for requests to the `users` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_user(self, user_id: int) -> GetUserResponse:
        """Fetch a user from the Ravy API.

        Parameters
        ----------
        user_id : int
            The user's Discord ID.

        Returns
        -------
        GetUserResponse
            The user's information model.
        """
        return GetUserResponse(
            await self._http.get(self._http.paths.users(user_id).route)
        )

    async def get_pronouns(self, user_id: int) -> GetPronounsResponse:
        """Fetch a user's pronouns from the Ravy API.

        Parameters
        ----------
        user_id : int
            The user's Discord ID.

        Returns
        -------
        GetPronounsResponse
            The user's pronouns model.
        """
        return GetPronounsResponse(
            await self._http.get(self._http.paths.users(user_id).pronouns)
        )

    async def get_bans(self, user_id: int) -> GetBansResponse:
        """Fetch a user's bans from the Ravy API.

        Parameters
        ----------
        user_id : int
            The user's Discord ID.

        Returns
        -------
        GetBansResponse
            The user's bans model.
        """
        return GetBansResponse(
            await self._http.get(self._http.paths.users(user_id).bans)
        )

    async def get_whitelists(self, user_id: int) -> GetWhitelistsResponse:
        """Fetch a user's whitelists from the Ravy API.

        Parameters
        ----------
        user_id : int
            The user's Discord ID.

        Returns
        -------
        GetWhitelistsResponse
            The user's whitelists model.
        """
        return GetWhitelistsResponse(
            await self._http.get(self._http.paths.users(user_id).whitelists)
        )

    async def get_reputation(self, user_id: int) -> GetReputationResponse:
        """Fetch a user's reputation from the Ravy API.

        Parameters
        ----------
        user_id : int
            The user's Discord ID.

        Returns
        -------
        GetReputationResponse
            The user's reputation model.
        """
        return GetReputationResponse(
            await self._http.get(self._http.paths.users(user_id).reputation)
        )
