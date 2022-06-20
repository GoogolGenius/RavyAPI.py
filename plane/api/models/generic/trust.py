# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""A generic model for trust."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Trust",)

from typing import Any


class Trust:
    """A generic model for trust.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    level: int
        TODO
    label: str
        TODO
    """

    __slots__: tuple[str, ...] = ("_data", "_level", "_label")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._level: int = data["level"]
        self._label: str = data["label"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def level(self) -> int:
        """TODO"""
        return self._level

    @property
    def label(self) -> str:
        """TODO"""
        return self._label
