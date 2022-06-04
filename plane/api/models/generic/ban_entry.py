from __future__ import annotations

__all__: tuple[str, ...] = (
    "BanEntryResponse",
    "BanEntryRequest",
)

from dataclasses import dataclass
from typing import Any


class BanEntryResponse:
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
    moderator : int
        User ID of the responsible moderator, usually Discord.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]
        self._reason_key: str | None = data.get("reason_key")
        self._moderator: int = int(data["moderator"])

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
    def moderator(self) -> int:
        """User ID of the responsible moderator, usually Discord."""
        return self._moderator


@dataclass
class BanEntryRequest:
    """Ban entry data model.

    Attributes
    ----------
    provider : str
        Source for where the user was banned.
    reason : str
        Why the user was banned.
    reason_key : str | None
        Machine-readable version of the reason - only present for providers ravy and dservices.
    moderator : str
        User ID of the responsible moderator, usually Discord.
    """

    provider: str
    reason: str
    moderator: int
    reason_key: str | None = None

    def from_model(self) -> dict[str, Any]:
        """Create a dictionary from the data model."""
        data = {
            "provider": self.provider,
            "reason": self.reason,
            "moderator": str(self.moderator),
        }

        if self.reason_key is not None:
            data["reason_key"] = self.reason_key

        return data
