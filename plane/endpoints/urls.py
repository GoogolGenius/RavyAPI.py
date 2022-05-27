from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

from typing import Any

from ..routes import Routes
from ..http import HTTPClient


class URLs:
    def __init__(self, http: HTTPClient, routes: Routes) -> None:
        self._http = http
        self._routes = routes

    async def get_url(self, url: str) -> dict[Any, Any]:
        return await self._http.get(self._routes.urls.url(url))
