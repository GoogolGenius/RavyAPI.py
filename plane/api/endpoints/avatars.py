from __future__ import annotations

__all__: tuple[str, ...] = ("Avatars",)

# import re

from typing_extensions import Literal

import aiohttp

from plane.api.models import CheckAvatarResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


# TODO: Test this endpoint properly. Maybe overload ? Hmm.
class Avatars(HTTPAwareEndpoint):
    """The implementation class for requests to the `guilds` route."""

    @with_permission_check("avatars")
    async def check_avatar(
        self: HTTPAwareEndpoint,
        avatar: str | bytes,
        threshold: float = 0.97,
        method: Literal["ssim", "phash"] = "phash",
    ) -> CheckAvatarResponse:
        """Check if avatar is fraudulent (Discord CDN).

        Parameters
        ----------
        avatar_url : str | bytes
            Link to the avatar, should start with cdn.discordapp.com; or bytes.
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

        if not isinstance(avatar, (str, bytes)):
            raise ValueError(
                'Parameter "avatar" must be of "str", "bytes" or derivative types'
            )

        if not 0 <= threshold <= 1:
            raise ValueError(
                'Parameter "threshold" must be of "float" or derivative between 0 and 1'
            )

        if method not in ("ssim", "phash"):
            raise ValueError(
                'Parameter "method" must be of "Literal" "str" type "ssim" | "phash"'
            )

        if isinstance(avatar, str):
            if not avatar.startswith("https://cdn.discordapp.com"):
                raise ValueError(
                    'Parameter "avatar_url" must start with "https://cdn.discordapp.com"'
                )

            return CheckAvatarResponse(
                await self._http.get(
                    self._http.paths.avatars.route,
                    params={
                        "avatar": avatar,
                        "threshold": threshold,
                        "method": method,
                    },
                )
            )

        form = aiohttp.FormData()
        form.add_field("avatar", avatar, content_type="application/octet-stream")

        headers = self._http.headers.copy()
        headers["Content-Type"] = "multipart/form-data"

        return CheckAvatarResponse(
            await self._http.get(
                self._http.paths.avatars.route,
                params={
                    "threshold": threshold,
                    "method": method,
                },
                data=form,
                headers=headers,
            )
        )
