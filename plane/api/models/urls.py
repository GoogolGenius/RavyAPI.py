# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("GetWebsiteResponse", "EditWebsiteRequest")

from dataclasses import dataclass
from typing import Any


class GetWebsiteResponse:
    """The website response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    is_fraudulent : bool
        Whether the URL is fraudulent.
    message : str
        The message about the URL.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._is_fraudulent: bool = data["isFraudulent"]
        self._message: str = data["message"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def is_fraudulent(self) -> bool:
        """Whether the URL is fraudulent."""
        return self._is_fraudulent

    @property
    def message(self) -> str:
        """The message about the URL."""
        return self._message


@dataclass(frozen=True)
class EditWebsiteRequest:
    """The request data model for editing a website."""

    is_fraudulent: bool
    message: str

    def from_model(self) -> dict[str, Any]:
        """Convert the data model to a dictionary."""
        return {
            "isFraudulent": self.is_fraudulent,
            "message": self.message,
        }
