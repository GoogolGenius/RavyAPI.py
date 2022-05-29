from __future__ import annotations

__all__: tuple[str, ...] = ("BanEntry",)

from typing import Any


class BanEntry:
    """Ban entry data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw JSON data from the API.
    provider : str
        Source for where the user was banned.
    reason : str
        Why the user was banned.
    reason_key : str | None
        Machine-readable version of the reason - only present for providers ravy and dservices.
    moderator : str
        User ID of the responsible moderator, usually Discord.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]
        self._reason_key: str | None = data.get("reason_key")
        self._moderator: str = data["moderator"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for where the user was banned."""
        return self._provider

    @property
    def reason(self) -> str:
        """Why the user was banned."""
        return self._reason

    @property
    def reason_key(self) -> str | None:
        """Machine-readable version of the reason - only present for providers ravy and dservices."""
        return self._reason_key

    @property
    def moderator(self) -> str:
        """User ID of the responsible moderator, usually Discord."""
        return self._moderator
