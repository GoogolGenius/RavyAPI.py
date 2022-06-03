from __future__ import annotations

__all__: tuple[str, ...] = ("KSoft",)

from plane.api.models import GetKSoftBanResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class KSoft(HTTPAwareEndpoint):
    """The implementation class for requests to the `ksoft` route."""

    @with_permission_check("ksoft.bans")
    async def get_ban(self: HTTPAwareEndpoint, user_id: int) -> GetKSoftBanResponse:
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
            await self._http.get(
                self._http.paths.ksoft.bans(user_id),
            )
        )
