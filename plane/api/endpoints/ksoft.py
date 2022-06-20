# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""Implementations for the ``ksoft`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("KSoft",)

from plane.api.models import GetKSoftBanResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class KSoft(HTTPAwareEndpoint):
    """A class with implementations for the ``ksoft`` endpoint.

    Methods
    -------
    get_ban(user_id: int) -> GetKSoftBanResponse
        TODO
    """

    @with_permission_check("ksoft.bans")
    async def get_ban(self: HTTPAwareEndpoint, user_id: int) -> GetKSoftBanResponse:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetKSoftBanResponse(
            await self._http.get(
                self._http.paths.ksoft.bans(user_id),
            )
        )
