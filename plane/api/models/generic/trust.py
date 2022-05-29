from __future__ import annotations

__all__: tuple[str, ...] = ("Trust",)

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
