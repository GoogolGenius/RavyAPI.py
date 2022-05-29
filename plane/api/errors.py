from __future__ import annotations
from typing import Any

__all__: tuple[str, ...] = ("HTTPException",)


class HTTPException(Exception):
    """The base exception class for HTTP errors.

    Attributes
    ----------
    status : int
        The HTTP status code of the error.
    exc_data : str | dict[str, Any]
        The error data from the API.
    """

    def __init__(self, status: int, exc_data: str | dict[str, Any]):
        """
        Parameters
        ----------
        status : int
            The HTTP status code of the error.
        exc_message : str
            The error message from the API.
        """
        self._status = status
        self._exc_data = exc_data

    def __str__(self) -> str:
        """Return the string representation of the exception."""
        if isinstance(self.exc_data, dict):
            return (
                f"({self.status}) {self.exc_data['error']}"
                f" - {self.exc_data['details']}"
            )

        return f"({self.status}) {self.exc_data}"

    @property
    def status(self) -> int:
        """The HTTP status code of the error."""
        return self._status

    @property
    def exc_data(self) -> str | dict[str, Any]:
        """The error data from the API."""
        return self._exc_data
