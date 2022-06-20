# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""API models for the ``avatars`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("CheckAvatarResponse",)

from typing import Any


class CheckAvatarResponse:
    """A model response from :func:`plane.api.endpoints.avatars.Avatars.check_avatar`.
    
    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    matched: bool
        TODO
    key: str
        TODO
    similarity: float
        TODO
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._matched: bool = data["isFraudulent"]
        self._key: str = data["message"]
        self._similarity: float = data["similarity"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def matched(self) -> bool:
        """TODO"""
        return self._matched

    @property
    def key(self) -> str:
        """TODO"""
        return self._key

    @property
    def similarity(self) -> float:
        """TODO"""
        return self._similarity
