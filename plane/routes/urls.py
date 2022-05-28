from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

from ..http import HTTPClient
from ..models import GetWebsiteResponse


class URLs:
    """The implementation class for requests to the `urls` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_website(self, url: str) -> GetWebsiteResponse:
        """Analyze a website URL by requesting the Ravy API.

        Parameters
        ----------
        url : str
            The URL to analyze.
        """
        return GetWebsiteResponse(
            await self._http.get(self._http.paths.urls(url).route)
        )