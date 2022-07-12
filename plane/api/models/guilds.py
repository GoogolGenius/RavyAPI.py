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
"""API models for the `guilds` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetGuildResponse",)

from typing import Any

from plane.api.models.generic import BanEntryResponse, Trust


class GetGuildResponse:
    """A model response from `plane.api.endpoints.guilds.Guilds.get_guild`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    trust: Trust
        The guild's `plane.api.models.generic.trust.Trust` trust model.
    bans: list[BanEntryResponse]
        A list of the guild's `plane.api.models.generic.ban_entry.BanEntryResponse` ban models.
    """

    __slots__: tuple[str, ...] = ("_data", "_trust", "_bans")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._trust: Trust = data["trust"]
        self._bans: list[BanEntryResponse] = [
            BanEntryResponse(ban) for ban in data["bans"]
        ]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(trust={self.trust!r}, bans={self.bans!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def trust(self) -> Trust:
        """The guild's `plane.api.models.generic.trust.Trust` trust model."""
        return self._trust

    @property
    def bans(self) -> list[BanEntryResponse]:
        """A list of the guilds's `plane.api.models.generic.ban_entry.BanEntryResponse` ban models."""
        return self._bans
