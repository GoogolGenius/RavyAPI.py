from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

from ..http import HTTPClient
from ..models import GetURLResponse


class URLs:
    """The implementation class for requests to the `urls` endpoint."""

    def __init__(self, http: HTTPClient) -> None:
        """
        Parameters
        ----------
        http : HTTPClient
            The internal HTTP client to use for requests.
        """
        self._http = http

    async def get_url(self, url: str) -> GetURLResponse:
        """Analyze a URL by requesting the Ravy API.

        Parameters
        ----------
        url : str
            The URL to analyze.
        """
        return GetURLResponse(await self._http.get(self._http.paths.urls.url(url)))
