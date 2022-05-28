from __future__ import annotations

__all__: tuple[str, ...] = ("GetTokenResponse",)

from typing import Any, Literal


class GetTokenResponse:
    """The token data model.

    Attributes
    ----------
    data : dict[Any, Any]
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

    def __init__(self, data: dict[Any, Any]) -> None:
        self.data = data
        self.user: str = data["user"]
        self.access: list[str] = data["access"]
        self.application: str = data["application"]
        self.type: Literal["ravy", "ksoft"] = data["type"]
