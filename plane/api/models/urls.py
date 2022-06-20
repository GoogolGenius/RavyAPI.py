# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""API models for the ``urls`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("GetWebsiteResponse", "EditWebsiteRequest")

from typing import Any


class GetWebsiteResponse:
    """A model response from :func:`plane.api.endpoints.urls.URLs.get_website`.

    Attributes
    ----------
    data: dict[str, Any]
        The raw data returned from the Ravy API.
    is_fraudulent: bool
        TODO
    message: str
        TODO
    """

    __slots__: tuple[str, ...] = ("_data", "_is_fraudulent", "_message")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._is_fraudulent: bool = data["isFraudulent"]
        self._message: str = data["message"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def is_fraudulent(self) -> bool:
        """TODO"""
        return self._is_fraudulent

    @property
    def message(self) -> str:
        """TODO"""
        return self._message


class EditWebsiteRequest:
    """A model request to :func:`plane.api.endpoints.urls.URLs.edit_website`.

    Parameters
    ----------
    is_fraudulent: bool
        TODO
    message: str
        TODO

    Attributes
    ----------
    is_fraudulent: bool
        TODO
    message: str
        TODO

    Methods
    -------
    from_model() -> dict[str, Any]
        Returns a JSON representation of the model.
    """

    __slots__: tuple[str, ...] = ("_is_fraudulent", "_message")

    def __init__(self, is_fraudulent: bool, message: str) -> None:
        """
        Parameters
        ----------
        is_fraudulent: bool
            TODO
        message: str
            TODO
        """
        self._is_fraudulent: bool = is_fraudulent
        self._message: str = message

    @property
    def is_fraudulent(self) -> bool:
        """TODO"""
        return self._is_fraudulent

    @property
    def message(self) -> str:
        """TODO"""
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
