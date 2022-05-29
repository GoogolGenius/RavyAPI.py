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
        """Get extensive user information.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetUserResponse
            The response from the API.
        """
        return GetUserResponse(
            await self._http.get(self._http.paths.users(user_id).route)
        )

    async def get_pronouns(self, user_id: int) -> GetPronounsResponse:
        """Get pronouns.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetPronounsResponse
            The response from the API.
        """
        return GetPronounsResponse(
            await self._http.get(self._http.paths.users(user_id).pronouns)
        )

    async def get_bans(self, user_id: int) -> GetBansResponse:
        """Get bans.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetBansResponse
            The response from the API.
        """
        return GetBansResponse(
            await self._http.get(self._http.paths.users(user_id).bans)
        )

    async def get_whitelists(self, user_id: int) -> GetWhitelistsResponse:
        """Get whitelists.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetWhitelistsResponse
            The response from the API.
        """
        return GetWhitelistsResponse(
            await self._http.get(self._http.paths.users(user_id).whitelists)
        )

    async def get_reputation(self, user_id: int) -> GetReputationResponse:
        """Get reputation.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetReputationResponse
            The response from the API.
        """
        return GetReputationResponse(
            await self._http.get(self._http.paths.users(user_id).reputation)
        )
