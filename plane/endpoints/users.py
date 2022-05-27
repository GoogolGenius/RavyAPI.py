from __future__ import annotations

__all__: tuple[str, ...] = ("Users",)

from typing import Any

from ..routes import Routes
from ..http import HTTPClient


class Users:
    def __init__(self, http: HTTPClient, routes: Routes) -> None:
        self._http = http
        self._routes = routes

    async def get_user(self, id: int) -> dict[Any, Any]:
        return await self._http.get(self._routes.users.user(id))

    async def get_pronouns(self, id: int) -> dict[Any, Any]:
        return await self._http.get(self._routes.users.pronouns(id))

    async def get_bans(self, id: int) -> dict[Any, Any]:
        return await self._http.get(self._routes.users.bans(id))

    async def get_whitelists(self, id: int) -> dict[Any, Any]:
        return await self._http.get(self._routes.users.whitelists(id))

    async def get_reputation(self, id: int) -> dict[Any, Any]:
        return await self._http.get(self._routes.users.reputation(id))
