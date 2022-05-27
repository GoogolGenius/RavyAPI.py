from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

from typing import Any

from ..http import HTTPClient


class URLs:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_url(self, url: str) -> dict[Any, Any]:
        return await self._http.get(self._http.routes.urls.url(url))
