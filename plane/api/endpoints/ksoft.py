from __future__ import annotations

__all__: tuple[str, ...] = ("KSoft",)

from ...http import HTTPClient
from ..models import GetKSoftBanResponse


class KSoft:
    """The implementation class for requests to the `ksoft` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_ban(self, user_id: int) -> GetKSoftBanResponse:
        """Get KSoft ban status.

        Parameters
        ----------
        user_id : int
            User ID of the user to look up.

        Returns
        -------
        GetKSoftBanResponse
            The response from the API.
        """
        return GetKSoftBanResponse(
            await self._http.get(self._http.paths.ksoft.bans(user_id))
        )
