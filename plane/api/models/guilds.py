# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""API models for the ``guilds`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetGuildResponse",)

from typing import Any

from plane.api.models.generic import Trust, BanEntryResponse


class GetGuildResponse:
    """A model response from :func:`plane.api.endpoints.guilds.Guilds.get_guild`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    trust: Trust
        The guild's :class:`plane.api.models.generic.trust.Trust` trust model.
    bans: list[BanEntryResponse]
        A list of the guilds's :class:`plane.api.models.generic.ban_entry.BanEntryResponse` ban models.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._trust: Trust = data["trust"]
        self._bans: list[BanEntryResponse] = [
            BanEntryResponse(ban) for ban in data["bans"]
        ]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def trust(self) -> Trust:
        """The guild's :class:`plane.api.models.generic.trust.Trust` trust model."""
        return self._trust

    @property
    def bans(self) -> list[BanEntryResponse]:
        """A list of the guilds's :class:`plane.api.models.generic.ban_entry.BanEntryResponse` ban models."""
        return self._bans
