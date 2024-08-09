# Copyright 2022-Present GoogolGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API models for the `tokens` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetTokenResponse",)

from typing import Any

from typing_extensions import Literal


class GetTokenResponse:
    """A model response from `ravyapi.api.endpoints.tokens.Tokens.get_token`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    user: str
        The user ID associated with the token.
    access: list[str]
        A list of valid permission nodes for the token.
    application: int
        The application ID registered to the token.
    token_type: Literal["ravy", "ksoft"]
        The type of the token, either "ravy" or "ksoft."
    """

    __slots__: tuple[str, ...] = (
        "_data",
        "_user",
        "_access",
        "_application",
        "_token_type",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._user: int = int(data["user"])
        self._access: list[str] = data["access"]
        self._application: int = int(data["application"])
        self._token_type: Literal["ravy", "ksoft"] = data["type"]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(user={self.user!r}, access={self.access!r}, application={self.application!r}, "
            f"token_type={self.token_type!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def user(self) -> int:
        """The user ID associated with the token."""
        return self._user

    @property
    def access(self) -> list[str]:
        """A list of valid permission nodes for the token."""
        return self._access

    @property
    def application(self) -> int:
        """The application ID registered to the token."""
        return self._application

    @property
    def token_type(self) -> Literal["ravy", "ksoft"]:
        """The type of the token, either "ravy" or "ksoft.\" """
        return self._token_type
