from __future__ import annotations

__all__: tuple[str, ...] = ("CheckAvatarResponse",)

from typing import Any


class CheckAvatarResponse:
    """The avatar response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    matched : bool
        Whether the avatar is matched.
    key : str
        The key of the avatar.
    similarity : float
        The similarity of the avatar.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._matched: bool = data["isFraudulent"]
        self._key: str = data["message"]
        self._similarity: float = data["similarity"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def matched(self) -> bool:
        """Whether the avatar is matched in the database."""
        return self._matched

    @property
    def key(self) -> str:
        """TODO: ..."""
        return self._key

    @property
    def similarity(self) -> float:
        """The similarity rating of the avatar."""
        return self._similarity
