from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)

from typing import Any

from ..http import HTTPClient


class Tokens:
    def __init__(self, http: HTTPClient) -> None:
        self._http = http

    async def get_token(self) -> dict[Any, Any]:
        return await self._http.get(self._http.routes.tokens.current())
