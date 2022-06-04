from __future__ import annotations

__all__: tuple[str, ...] = ("Avatars",)

# import re

from typing_extensions import Literal

from plane.api.models import CheckAvatarResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class Avatars(HTTPAwareEndpoint):
    """The implementation class for requests to the `guilds` route."""

    @with_permission_check("avatars")
    async def check_avatar(
        self: HTTPAwareEndpoint,
        avatar_url: str,
        threshold: float = 0.97,
        method: Literal["ssim", "phash"] = "phash",
    ) -> CheckAvatarResponse:
        """Check if avatar is fraudulent (Discord CDN).

        Parameters
        ----------
        avatar_url : str
            Link to the avatar, should start with cdn.discordapp.com.
        threshold : float
            How similar the avatar needs to be for it to match (0-1, default 0.97).
        method : Literal["ssim", "phash"]
            Which method to use for matching the avatars ("ssim" or "phash", default is "phash")

        Returns
        -------
        CheckAvatarResponse
            The response from the API.
        """
        # if re.match(r"\^https:\/\/cdn.discordapp.com\i", avatar_url) is None:
        #     raise ValueError('Parameter "avatar_url" must start with "https://cdn.discordapp.com"')

        if not avatar_url.startswith("https://cdn.discordapp.com"):
            raise ValueError(
                'Parameter "avatar_url" must start with "https://cdn.discordapp.com"'
            )

        if not 0 <= threshold <= 1:
            raise ValueError(
                'Parameter "threshold" must be of "float" or derivative between 0 and 1'
            )

        if method not in ("ssim", "phash"):
            raise ValueError(
                'Parameter "method" must be of "Literal" "str" type "ssim" | "phash"'
            )

        return CheckAvatarResponse(
            await self._http.get(
                self._http.paths.avatars.route,
                params={
                    "avatar": avatar_url,
                    "threshold": threshold,
                    "method": method,
                },
            )
        )
