from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

import urllib.parse

from typing import TYPE_CHECKING

from ..models import GetWebsiteResponse
from ...utils import with_permission_check

if TYPE_CHECKING:
    from ...http import HTTPClient


class URLs:
    """The implementation class for requests to the `urls` route."""

    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    @with_permission_check("urls.cached")
    async def get_website(self, url: str, encode: bool = True) -> GetWebsiteResponse:
        """Get website information.

        Parameters
        ----------
        url : str
            The url-encoded url to look up.
        encode : bool
            Whether to auto-encode the url, True by default.
        """
        if encode:
            url = urllib.parse.quote_plus(url)

        return GetWebsiteResponse(
            await self._http.get(self._http.paths.urls(url).route)
        )
