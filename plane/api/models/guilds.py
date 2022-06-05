# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("GetGuildResponse",)

from typing import Any

from plane.api.models.generic import Trust, BanEntryResponse


class GetGuildResponse:
    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._trust: Trust = data["trust"]
        self._bans: list[BanEntryResponse] = [
            BanEntryResponse(ban) for ban in data["bans"]
        ]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def trust(self) -> Trust:
        """The trust model of the guild."""
        return self._trust

    @property
    def bans(self) -> list[BanEntryResponse]:
        """The ban entry model of the guild."""
        return self._bans
