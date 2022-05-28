from __future__ import annotations

__all__: tuple[str, ...] = ("GetURLResponse",)

from typing import Any


class GetURLResponse:
    """The URL data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    is_fraudulent : str
        Whether the URL is fraudulent.
    message : str
        The message about the URL.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._is_fraudulent: str = data["isFraudulent"]
        self._message = data["message"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def is_fraudulent(self) -> str:
        """Whether the URL is fraudulent."""
        return self._is_fraudulent

    @property
    def message(self) -> str:
        """The message about the URL."""
        return self._message
