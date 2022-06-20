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

from typing import Any


class BanEntryResponse:
    """A generic model for ban entry responses.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    provider: str
        Source for where the user or guild was banned.
    reason: str
        Why the user or guild was banned.
    reason_key: str | None
        Machine-readable version of the reason - only present for providers ravy and dservices.
    moderator: int
        User ID of the responsible moderator, usually Discord.
    """

    __slots__: tuple[str, ...] = (
        "_data",
        "_provider",
        "_reason",
        "_reason_key",
        "_moderator",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]
        self._reason_key: str | None = data.get("reason_key")
        self._moderator: int = int(data["moderator"])

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(provider={self.provider!r}, reason={self.reason!r}, "
            f"reason_key={self.reason_key!r}, moderator={self.moderator!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for where the user or guild was banned."""
        return self._provider

    @property
    def reason(self) -> str:
        """Why the user or guild was banned."""
        return self._reason

    @property
    def reason_key(self) -> str | None:
        """Machine-readable version of the reason - only present for providers ravy and dservices."""
        return self._reason_key

    @property
    def moderator(self) -> int:
        """User ID of the responsible moderator, usually Discord."""
        return self._moderator


class BanEntryRequest:
    """A generic model for ban entry requests.

    Parameters
    ----------
    provider: str
        Source for where the user or guild is banned.
    reason: str
        Why the user or guild is banned.
    moderator: int
        User ID of the responsible moderator, usually Discord.
    reason_key: str | None
        Machine-readable version of the reason - only present for providers ravy and dservices.

    Attributes
    ----------
    provider: str
        Source for where the user or guild is banned.
    reason: str
        Why the user or guild is banned.
    moderator: int
        User ID of the responsible moderator, usually Discord.
    reason_key: str | None
        Machine-readable version of the reason - only present for providers ravy and dservices.

    Methods
    -------
    to_json() -> dict[str, Any]
        Returns a JSON representation of the model.
    """

    __slots__: tuple[str, ...] = ("_provider", "_reason", "_moderator", "_reason_key")

    def __init__(
        self, provider: str, reason: str, moderator: int, reason_key: str | None = None
    ) -> None:
        """
        Parameters
        ----------
        provider: str
            Source for where the user or guild is banned.
        reason: str
            Why the user or guild is banned.
        moderator: int
            User ID of the responsible moderator, usually Discord.
        reason_key: str | None
            Machine-readable version of the reason - only present for providers ravy and dservices.
        """
        self._provider: str = provider
        self._reason: str = reason
        self._moderator: int = moderator
        self._reason_key: str | None = reason_key

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(provider={self.provider!r}, reason={self.reason!r}, "
            f"moderator={self.moderator!r}, reason_key={self.reason_key!r})"
        )

    @property
    def provider(self) -> str:
        """Source for where the user or guild is banned."""
        return self._provider

    @property
    def reason(self) -> str:
        """Why the user or guild is banned."""
        return self._reason

    @property
    def moderator(self) -> int:
        """User ID of the responsible moderator, usually Discord."""
        return self._moderator

    @property
    def reason_key(self) -> str | None:
        """Machine-readable version of the reason - only present for providers ravy and dservices."""
        return self._reason_key

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
