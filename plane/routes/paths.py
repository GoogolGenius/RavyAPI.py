from __future__ import annotations

__all__: tuple[str, ...] = ("Paths",)

from ..const import BASE_URL


class Paths:
    """A base class for all Ravy API URL route paths."""

    @property
    def base(self) -> str:
        """The base URL for the Ravy API."""
        return BASE_URL

    def guilds(self, guild_id: int) -> Guilds:
        """Route paths for the main `guilds` route."""
        return Guilds(guild_id)

    def tokens(self, token: str) -> Tokens:
        """Route paths for the main `tokens` route."""
        return Tokens(token)

    def urls(self, url: str) -> URLs:
        """Route paths for the main `urls` route."""
        return URLs(url)

    def users(self, user_id: int) -> Users:
        """Route paths for the main `users` route."""
        return Users(user_id)


class Guilds:
    """A class containing route paths for the `guilds` main route."""

    def __init__(self, guild_id: int) -> None:
        self._guild_id = guild_id
        self._route = f"/guilds/{self._guild_id}"

    @property
    def route(self) -> str:
        """The route path for the `guilds` route."""
        return self._route

    @property
    def guild_id(self) -> int:
        """The guild ID passed in to the `guilds` route"""
        return self._guild_id


class Tokens:
    """A class containing route paths for the `tokens` main route."""

    def __init__(self, token: str) -> None:
        # Token passed in for the property. Any point since this is internal ?
        # Very questionable design decisions by myself... lol
        self._token = token
        self._route = "/tokens/@current"

    @property
    def route(self) -> str:
        """The route path for the `tokens` route."""
        return self._route

    @property
    def token(self) -> str:
        """The token used by the HTTPClient (internal)."""
        return self._token


class URLs:
    """A class containing route paths for the `urls` main route."""

    def __init__(self, url: str) -> None:
        self._url = url
        self._route = f"/urls/{self._url}"

    @property
    def route(self) -> str:
        """The route path for the `urls` route"""
        return self._route

    @property
    def url(self) -> str:
        """The website URL passed in to the `urls` route"""
        return self._url


class Users:
    """A class containing route paths for the `users` main route"""

    def __init__(self, user_id: int) -> None:
        self._user_id = user_id
        self._route = f"/users/{self._user_id}"

    @property
    def route(self) -> str:
        """The route path for the `users` route"""
        return self._route

    @property
    def user_id(self) -> int:
        """The user ID passed in to the `users` route"""
        return self._user_id

    @property
    def pronouns(self) -> str:
        """The URL strcture for the child route `pronouns` of `users`."""
        return self._route + "/pronouns"

    @property
    def bans(self) -> str:
        """The URL structure for the child route `bans` of `users`."""
        return self._route + "/bans"

    @property
    def whitelists(self) -> str:
        """The URL structure for the child route `whitelists` of `users`."""
        return self._route + "/whitelists"

    @property
    def reputation(self) -> str:
        return self._route + "/rep"
