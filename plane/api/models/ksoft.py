from __future__ import annotations

__all__: tuple[str, ...] = ("GetKSoftBanResponse",)

from typing import Any


class GetKSoftBanResponse:
    """The data model response for a KSoft ban."""

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._found: bool = data["found"]
        user_id = data.get("id")
        self._user_id: int | None = int(user_id) if user_id else None
        self._tag: str | None = data.get("tag")
        self._reason: str | None = data.get("reason")
        self._proof: str | None = data.get("proof")
        moderator: str | None = data.get("moderator")
        self._moderator: int | None = int(moderator) if moderator else None
        self._severe: bool | None = data.get("severe")
        self._timestamp: str | None = data.get("timestamp")

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API.

        !!! note
            Raw `str` IDs are not converted to `int`.
        """
        return self._data

    @property
    def found(self) -> bool:
        """Whether the user was found."""
        return self._found

    @property
    def user_id(self) -> int | None:
        """The user's ID.

        !!! note
            This is casted from raw `str` to `int` type.
        """
        return self._user_id

    @property
    def tag(self) -> str | None:
        """The user's tag."""
        return self._tag

    @property
    def reason(self) -> str | None:
        """The ban reason."""
        return self._reason

    @property
    def proof(self) -> str | None:
        """The proof."""
        return self._proof

    @property
    def moderator(self) -> int | None:
        """The moderator's name.

        !!! note
            This is casted from raw `str` to `int` type.
        """
        return self._moderator

    @property
    def severe(self) -> bool | None:
        """Whether the ban is severe."""
        return self._severe

    @property
    def timestamp(self) -> str | None:
        """The timestamp of the ban."""
        return self._timestamp
