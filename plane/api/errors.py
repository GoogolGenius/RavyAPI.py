# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""Exceptions raised when an error is encountered during API calls."""

from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPException", "AccessException")

from typing import Any


class HTTPException(Exception):
    """A base class for all HTTP exceptions.

    Attributes
    ----------
    status : int
        The HTTP status code of the response.
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    def __init__(self, status: int, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        status : int
            The HTTP status code of the error.
        exc_data : str
            The error message from the API.
        """
        super().__init__()
        self._status: int = status
        self._exc_data: str | dict[str, Any] = exc_data

    def __str__(self) -> str:
        if isinstance(self.exc_data, dict):
            return (
                f"({self.status}) {self.exc_data['error']}"
                f" - {self.exc_data['details']}"
            )

        return f"({self.status}) {self.exc_data}"

    @property
    def status(self) -> int:
        """The HTTP status code of the response."""
        return self._status

    @property
    def exc_data(self) -> str | dict[str, Any]:
        """The error data returned by the Ravy API."""
        return self._exc_data


class AccessException(Exception):
    """A class denoting an exception raised when required permissions are not satisfied.
    
    Attributes
    ----------
    required : str
        The required permissions for a path route.
    """
    def __init__(self, required: str) -> None:
        """
        Parameters
        ----------
        required : list[str]
            The permissions that were needed.
        """
        super().__init__()
        self._required: str = required

    def __str__(self) -> str:
        return f'Insufficient permissions accessing path route requiring "{self.required}"'

    @property
    def required(self) -> str:
        """The required permissions for a path route."""
        return self._required
