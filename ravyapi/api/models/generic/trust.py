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
        From 0-6, higher is better, default is 3.
    label: str
        What the number means.
    """

    __slots__: tuple[str, ...] = ("_data", "_level", "_label")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._level: int = data["level"]
        self._label: str = data["label"]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(level={self.level!r}, label={self.label!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def level(self) -> int:
        """From 0-6, higher is better, default is 3."""
        return self._level

    @property
    def label(self) -> str:
        """What the number means."""
        return self._label
