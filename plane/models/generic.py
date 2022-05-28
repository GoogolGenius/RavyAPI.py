from __future__ import annotations

__all__: tuple[str, ...] = ("Trust", "BanEntry")

from typing import Any


class Trust:
    """The trust data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    level : int
        From 0-6, higher is better, default is 3.
    label : str
        What the number means.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._level: int = data["level"]
        self._label: str = data["label"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def level(self) -> int:
        """From 0-6, higher is better."""
        return self._level

    @property
    def label(self) -> str:
        """What the number means."""
        return self._label


class BanEntry:
    """The ban entry data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    provider : str
        Source for where the user is banned.
    reason : str
        Why the user is banned, usually STAFF.
    reason_key : str | None
        Machine-readable version of the reason - only present for providers ravy and dservices
    moderator : str
        User ID of the responsible moderator, usually Discord
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]
        self._reason_key: str | None = data["reason_key"]
        self._moderator: str = data["moderator"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for where the user is banned."""
        return self._provider

    @property
    def reason(self) -> str:
        """Why the user is banned, usually STAFF."""
        return self._reason

    @property
    def reason_key(self) -> str | None:
        """Machine-readable version of the reason - only present for providers ravy and dservices."""
        return self._reason_key

    @property
    def moderator(self) -> str:
        """User ID of the responsible moderator, usually Discord."""
        return self._moderator
