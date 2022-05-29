from __future__ import annotations
from typing import Any

__all__: tuple[str, ...] = ("HTTPException",)


class HTTPException(Exception):
    """The base exception class for HTTP errors.

    Attributes
    ----------
    status : int
        The HTTP status code of the error.
    exc_message : str | dict[str, Any]
        The error message from the API.
    """

    def __init__(self, status: int, exc_message: str | dict[str, Any]):
        """
        Parameters
        ----------
        status : int
            The HTTP status code of the error.
        exc_message : str
            The error message from the API.
        """
        self._status = status
        self._exc_message = exc_message

    def __str__(self) -> str:
        """Return the string representation of the exception."""
        if isinstance(self.exc_message, dict):
            return (
                f"({self.status}) {self.exc_message['error']}"
                f" - {self.exc_message['details']}"
            )

        return f"({self.status}) {self.exc_message}"

    @property
    def status(self) -> int:
        """The HTTP status code of the error."""
        return self._status

    @property
    def exc_message(self) -> str | dict[str, Any]:
        """The error message from the API."""
        return self._exc_message
