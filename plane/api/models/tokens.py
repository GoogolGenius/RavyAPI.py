from __future__ import annotations

__all__: tuple[str, ...] = ("GetTokenResponse",)

from typing import Any
from typing_extensions import Literal


class GetTokenResponse:
    """The token response data model.

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
    token_type : Literal["ravy", "ksoft"]
        The type of the token.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._user: str = data["user"]
        self._access: list[str] = data["access"]
        self._application: int = int(data["application"])
        self._token_type: Literal["ravy", "ksoft"] = data["type"]

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
        """The permission nodes of the token."""
        return self._access

    @property
    def application(self) -> int:
        """The application ID of the token."""
        return self._application

    @property
    def token_type(self) -> Literal["ravy", "ksoft"]:
        """The type of the token, either 'ravy or 'ksoft.'"""
        return self._token_type
