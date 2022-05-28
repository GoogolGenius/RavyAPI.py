from __future__ import annotations

__all__: tuple[str, ...] = ("GetURLResponse",)

from typing import Any


class GetURLResponse:
    """The URL data model.

    Attributes
    ----------
    data : dict[Any, Any]
        The raw data from the API.
    is_fraudulent : str
        Whether the URL is fraudulent.
    message : str
        The message about the URL.
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.data = data
        self.is_fraudulent: str = data["isFraudulent"]
        self.message = data["message"]
