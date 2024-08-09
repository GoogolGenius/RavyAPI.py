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
"""API models for the `urls` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetWebsiteResponse", "EditWebsiteRequest")

from typing import Any


class GetWebsiteResponse:
    """A model response from `ravyapi.api.endpoints.urls.URLs.get_website`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    is_fraudulent: bool
        Whether the website is fraudulent.
    message: str
        An informational message about the website.
    """

    __slots__: tuple[str, ...] = ("_data", "_is_fraudulent", "_message")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._is_fraudulent: bool = data["isFraudulent"]
        self._message: str = data["message"]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(is_fraudulent={self.is_fraudulent!r}, message={self.message!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def is_fraudulent(self) -> bool:
        """Whether the website is fraudulent."""
        return self._is_fraudulent

    @property
    def message(self) -> str:
        """An informational message about the website."""
        return self._message


class EditWebsiteRequest:
    """A model request to `ravyapi.api.endpoints.urls.URLs.edit_website`.

    Parameters
    ----------
    is_fraudulent: bool
        Whether the website is fraudulent.
    message: str
        An informational message about the website.

    Attributes
    ----------
    is_fraudulent: bool
        Whether the website is fraudulent.
    message: str
        An informational message about the website.
    """

    __slots__: tuple[str, ...] = ("_is_fraudulent", "_message")

    def __init__(self, is_fraudulent: bool, message: str) -> None:
        """
        Parameters
        ----------
        is_fraudulent: bool
            Whether the website is fraudulent.
        message: str
            An informational message about the website.
        """
        self._is_fraudulent: bool = is_fraudulent
        self._message: str = message

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(is_fraudulent={self.is_fraudulent!r}, message={self.message!r})"
        )

    @property
    def is_fraudulent(self) -> bool:
        """Whether the website is fraudulent."""
        return self._is_fraudulent

    @property
    def message(self) -> str:
        """An informational message about the website."""
        return self._message

    def to_json(self) -> dict[str, Any]:
        """Returns a JSON representation of the model.

        Returns
        -------
        dict[str, Any]
            A JSON representation of the model.
        """
        return {
            "isFraudulent": self.is_fraudulent,
            "message": self.message,
        }
