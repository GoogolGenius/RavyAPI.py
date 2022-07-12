# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implementations for the `guilds` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Guilds",)

from plane.api.models import GetGuildResponse
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class Guilds(HTTPAwareEndpoint):
    """A class with implementations for the `guilds` endpoint."""

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
            If any parameters are of invalid types.

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
