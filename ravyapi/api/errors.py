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
"""Exceptions raised when an error is encountered during API calls."""

from __future__ import annotations

__all__: tuple[str, ...] = (
    "AccessError",
    "BadRequestError",
    "ForbiddenError",
    "HTTPError",
    "NotFoundError",
    "TooManyRequestsError",
    "UnauthorizedError",
)

from typing import Any


class HTTPError(Exception):
    """A base class for all HTTP exceptions.

    Parameters
    ----------
    status : int
        The HTTP status code of the response.
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.

    Attributes
    ----------
    status : int
        The HTTP status code of the response.
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    __slots__: tuple[str, ...] = ("_status", "_exc_data")

    def __init__(self, status: int, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        status : int
            The HTTP status code of the response.
        exc_data : str | dict[str, Any]
            The error data returned by the Ravy API.
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


class AccessError(Exception):
    """A class denoting an exception raised when required permission is not satisfied.

    Attributes
    ----------
    required : str
        The required permission for a path route.
    """

    __slots__: tuple[str, ...] = ("_required",)

    def __init__(self, required: str) -> None:
        """
        Parameters
        ----------
        required : str
            The permission that was needed.
        """
        super().__init__()
        self._required: str = required

    def __str__(self) -> str:
        return (
            f'Insufficient permissions accessing path route requiring "{self.required}"'
        )

    @property
    def required(self) -> str:
        """The required permission for a path route."""
        return self._required


class BadRequestError(HTTPError):
    """A class denoting an exception raised when a bad request is made.

    Attributes
    ----------
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    __slots__: tuple[str, ...] = ("_exc_data",)

    def __init__(self, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        exc_data : str | dict[str, Any]
            The error data returned by the Ravy API.
        """
        super().__init__(400, exc_data)


class UnauthorizedError(HTTPError):
    """A class denoting an exception raised when an unauthorized request is made.

    Attributes
    ----------
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    __slots__: tuple[str, ...] = ("_exc_data",)

    def __init__(self, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        exc_data : str | dict[str, Any]
            The error data returned by the Ravy API.
        """
        super().__init__(401, exc_data)


class ForbiddenError(HTTPError):
    """A class denoting an exception raised when a forbidden request is made.

    Attributes
    ----------
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    __slots__: tuple[str, ...] = ("_exc_data",)

    def __init__(self, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        exc_data : str | dict[str, Any]
            The error data returned by the Ravy API.
        """
        super().__init__(403, exc_data)


class NotFoundError(HTTPError):
    """A class denoting an exception raised when a resource is not found.

    Attributes
    ----------
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    __slots__: tuple[str, ...] = ("_exc_data",)

    def __init__(self, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        exc_data : str | dict[str, Any]
            The error data returned by the Ravy API.
        """
        super().__init__(404, exc_data)


class TooManyRequestsError(HTTPError):
    """A class denoting an exception raised when a request is made too frequently.

    Attributes
    ----------
    exc_data : str | dict[str, Any]
        The error data returned by the Ravy API.
    """

    __slots__: tuple[str, ...] = ("_exc_data",)

    def __init__(self, exc_data: str | dict[str, Any]) -> None:
        """
        Parameters
        ----------
        exc_data : str | dict[str, Any]
            The error data returned by the Ravy API.
        """
        super().__init__(429, exc_data)
