from __future__ import annotations

__all__: tuple[str, ...] = ("Routes",)

from .const import BASE_URL


class Routes:
    @property
    def base(self) -> str:
        return BASE_URL

    @property
    def users(self) -> Users:
        return Users()

    @property
    def urls(self) -> URLs:
        return URLs()

    @property
    def tokens(self) -> Tokens:
        return Tokens()


class Users:
    _ENDPOINT_URL = "/users"

    def user(self, id: int) -> str:
        return self._ENDPOINT_URL + f"/{id}"

    def pronouns(self, id: int) -> str:
        return self.user(id) + "/pronouns"

    def bans(self, id: int) -> str:
        return self.user(id) + "/bans"

    def whitelists(self, id: int) -> str:
        return self.user(id) + "/whitelists"

    def reputation(self, id: int) -> str:
        return self.user(id) + "/rep"


class URLs:
    _ENDPOINT_URL = "/urls"

    def url(self, url: str) -> str:
        return self._ENDPOINT_URL + f"/{url}"


class Tokens:
    _ENDPOINT_URL = "/tokens"

    # Does this make sense as a property or function?
    def current(self) -> str:
        return self._ENDPOINT_URL + "/@current"
