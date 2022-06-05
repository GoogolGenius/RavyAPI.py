# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("CheckAvatarResponse",)

from typing import Any


class CheckAvatarResponse:
    """The avatar response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    matched : bool
        Whether the avatar is matched.
    key : str
        The key of the avatar.
    similarity : float
        The similarity of the avatar.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._matched: bool = data["isFraudulent"]
        self._key: str = data["message"]
        self._similarity: float = data["similarity"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def matched(self) -> bool:
        """Whether the avatar is matched in the database."""
        return self._matched

    @property
    def key(self) -> str:
        """TODO: Ask Ravy about this."""
        return self._key

    @property
    def similarity(self) -> float:
        """The similarity rating of the avatar."""
        return self._similarity
