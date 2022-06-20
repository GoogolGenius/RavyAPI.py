# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""The implementations for the ``avatars`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Avatars",)

import urllib.parse

from typing_extensions import Literal

import aiohttp

from plane.api.models import CheckAvatarResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


# TODO: Test this endpoint properly when Ravy authorizes me for permissions!
# Still waiting, lol. Patience, young padawan.
class Avatars(HTTPAwareEndpoint):
    """A class with implementations for the ``avatars`` endpoint.

    Methods
    -------
    check_avatar(avatar: str | bytes, threshold: float = 0.97, method: Literal["ssim", "phash"] = "phash") -> CheckAvatarResponse
        Check if avatar is fraudulent.
    """

    __slots__: tuple[str, ...] = ()

    @with_permission_check("avatars")
    async def check_avatar(
        self: HTTPAwareEndpoint,
        avatar: str | bytes,
        threshold: float = 0.97,
        method: Literal["ssim", "phash"] = "phash",
    ) -> CheckAvatarResponse:
        """Check if avatar is fraudulent.

        Parameters
        ----------
        avatar : str | bytes
            Link to the avatar, should start with "cdn.discordapp.com" or the avatar to query, as an octet stream.
        threshold : float = 0.97
            How similar the avatar needs to be for it to match (0-1, default 0.97).
        method : Literal["ssim", "phash"] = "phash"
            Which method to use for matching the avatars ("ssim" or "phash", default is "phash").

        Raises
        ------
        TypeError
            If any parameters are invalid type.
        ValueError
            If any parameters are invalid value.

        Returns
        -------
        CheckAvatarResponse
            A model response from :meth:`plane.api.endpoints.avatars.Avatars.check_avatar`. Located as :class:`plane.api.models.avatars.CheckAvatarResponse`.
        """
        if not isinstance(avatar, (str, bytes)):
            raise TypeError('Parameter "avatar" must be of type "str" or "bytes"')

        if not avatar:
            raise ValueError('Parameter "avatar" must not be empty')

        if not 0 <= threshold <= 1:
            raise ValueError(
                'Parameter "threshold" must be of type "float" between 0 and 1'
            )

        if method not in ("ssim", "phash"):
            raise ValueError('Parameter "method" must be either "ssim" or "phash"')

        if isinstance(avatar, str):
            if urllib.parse.urlparse(avatar).hostname != "cdn.discordapp.com":
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

        return CheckAvatarResponse(
            await self._http.post(
                self._http.paths.avatars.route,
                params={
                    "threshold": threshold,
                    "method": method,
                },
                data=form(),
            )
        )
