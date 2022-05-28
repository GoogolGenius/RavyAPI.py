from __future__ import annotations

__all__: tuple[str, ...] = ("GetTokenResponse",)

from typing import Any
from typing_extensions import Literal


class GetTokenResponse:
    """The token data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    user : str
        The user of the token.
    access : list[str]
        The access of the token.
    application : str
        The application of the token.
    type : “ravy“ | “ksoft“
        The type of the token.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._user: str = data["user"]
        self._access: list[str] = data["access"]
        self._application: str = data["application"]
        self._type: Literal["ravy", "ksoft"] = data["type"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def user(self) -> str:
        """The user of the token."""
        return self._user

    @property
    def access(self) -> list[str]:
        """The access of the token."""
        return self._access

    @property
    def application(self) -> str:
        """The application ID of the token."""
        return self._application

    @property
    def type(self) -> Literal["ravy", "ksoft"]:
        """The type of the token."""
        return self._type
