from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPException",)


class HTTPException(Exception):
    """The base exception class for HTTP errors.

    Attributes
    ----------
    status : int
        The HTTP status code of the error.
    exc_message : str
        The error message from the API.
    """

    def __init__(self, status: int, exc_message: str):
        """
        Parameters
        ----------
        status : int
            The HTTP status code of the error.
        exc_message : str
            The error message from the API.
        """
        self.status = status
        self.exc_message = exc_message

    def __str__(self) -> str:
        """Return the string representation of the exception."""
        return f"{self.status}\n{self.exc_message}"
