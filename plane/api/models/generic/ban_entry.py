# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""Generic models for ban entries."""

from __future__ import annotations

__all__: tuple[str, ...] = ("BanEntryResponse", "BanEntryRequest")

from dataclasses import dataclass
from typing import Any


class BanEntryResponse:
    """A generic model for ban entry responses.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    provider: str
        TODO
    reason: str
        TODO
    reason_key: str | None
        TODO
    moderator: int
        TODO
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]
        self._reason_key: str | None = data.get("reason_key")
        self._moderator: int = int(data["moderator"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def provider(self) -> str:
        """TODO"""
        return self._provider

    @property
    def reason(self) -> str:
        """TODO"""
        return self._reason

    @property
    def reason_key(self) -> str | None:
        """TODO"""
        return self._reason_key

    @property
    def moderator(self) -> int:
        """TODO"""
        return self._moderator


@dataclass(frozen=True)
class BanEntryRequest:
    """A generic model for ban entry requests.

    Attributes
    ----------
    provider: str
        TODO
    reason: str
        TODO
    moderator: int
        TODO
    reason_key: str | None
        TODO

    Methods
    -------
    to_json() -> dict[str, Any]
        Returns a JSON representation of the model.
    """

    provider: str
    """TODO"""
    reason: str
    """TODO"""
    moderator: int
    """TODO"""
    reason_key: str | None = None
    """TODO"""

    def to_json(self) -> dict[str, Any]:
        """Returns a JSON representation of the model.

        Returns
        -------
        dict[str, Any]
            A JSON representation of the model.
        """
        data = {
            "provider": self.provider,
            "reason": self.reason,
            "moderator": str(self.moderator),
        }

        if self.reason_key is not None:
            data["reason_key"] = self.reason_key

        return data
