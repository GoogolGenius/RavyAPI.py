# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""API models for the ``tokens`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetTokenResponse",)

from typing import Any
from typing_extensions import Literal


class GetTokenResponse:
    """A model response from :func:`plane.api.endpoints.tokens.Tokens.get_token`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    user: str
        TODO
    access: list[str]
        TODO
    application: int
        TODO
    token_type: Literal["ravy", "ksoft"]
        TODO
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._user: str = data["user"]
        self._access: list[str] = data["access"]
        self._application: int = int(data["application"])
        self._token_type: Literal["ravy", "ksoft"] = data["type"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def user(self) -> str:
        """TODO"""
        return self._user

    @property
    def access(self) -> list[str]:
        """TODO"""
        return self._access

    @property
    def application(self) -> int:
        """TODO"""
        return self._application

    @property
    def token_type(self) -> Literal["ravy", "ksoft"]:
        """TODO"""
        return self._token_type
