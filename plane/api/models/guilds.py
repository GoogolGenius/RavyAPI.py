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
        return self._data

    @property
    def trust(self) -> Trust:
        return self._trust

    @property
    def bans(self) -> list[BanEntryResponse]:
        return self._bans
