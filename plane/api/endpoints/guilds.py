# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""The implementations for the `guilds` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Guilds",)

from plane.api.models import GetGuildResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class Guilds(HTTPAwareEndpoint):
    """A class with implementations for the `guilds` endpoint.

    Methods
    -------
    get_guild(guild_id: int) -> GetGuildResponse
        Get extensive guild information.
    """

    __slots__: tuple[str, ...] = ()

    @with_permission_check("guilds")
    async def get_guild(self: HTTPAwareEndpoint, guild_id: int) -> GetGuildResponse:
        """Get extensive guild information.

        Parameters
        ----------
        guild_id : int
            Guild ID of the guild to look up.

        Raises
        ------
        TypeError
            If any parameters are invalid type.

        Returns
        -------
        GetGuildResponse
            A model response from `plane.api.endpoints.guilds.Guilds.get_guild`.
            Located as `plane.api.models.guilds.GetGuildResponse`.
        """
        if not isinstance(guild_id, int):
            raise TypeError('Parameter "guild_id" must be of type "int"')

        return GetGuildResponse(
            await self._http.get(
                self._http.paths.guilds(guild_id).route,
            )
        )
