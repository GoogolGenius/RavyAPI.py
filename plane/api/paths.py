from __future__ import annotations

__all__: tuple[str, ...] = ("Paths",)

from ..const import BASE_URL


class Paths:
    """A base class for all Ravy API URL route paths."""

    @property
    def avatars(self) -> Avatars:
        """Route paths for the main `avatars` route."""
        return Avatars()

    @staticmethod
    def guilds(guild_id: int) -> Guilds:
        """Route paths for the main `guilds` route."""
        return Guilds(guild_id)

    @property
    def ksoft(self) -> KSoft:
        """Route paths for the main `ksoft` route."""
        return KSoft()

    @property
    def tokens(self) -> Tokens:
        """Route paths for the main `tokens` route."""
        return Tokens()

    @staticmethod
    def urls(url: str) -> URLs:
        """Route paths for the main `urls` route."""
        return URLs(url)

    @staticmethod
    def users(user_id: int) -> Users:
        """Route paths for the main `users` route."""
        return Users(user_id)


class Avatars:
    """Route paths for the `avatars` route.

    This is the same as the `base` url of the Ravy API; however,
    this is created as a more concrete class for avatars.
    """

    @property
    def route(self) -> str:
        """The route path for the `avatars` route."""
        return BASE_URL


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


class KSoft:
    """Route paths for the `ksoft` route.

    This class was created with expansion in mind to avoid potential breakage.
    However, with the current Ravy API this might look a bit strange compared
    to the other route classes.
    """

    def __init__(self) -> None:
        self._route = "/ksoft"

    @property
    def route(self) -> str:
        """The route path for the `avatars` route."""
        return self._route

    def bans(self, user_id: int) -> str:
        """Route paths for the `bans` route.

        Parameters
        ----------
        user_id : int
            The Discord ID of the user.
        """
        return f"{self._route}/bans/{user_id}"


class Tokens:
    """A class containing route paths for the `tokens` main route."""

    @property
    def route(self) -> str:
        """The route path for the `tokens` route."""
        return "/tokens/@current"


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
        return f"{self._route}/pronouns"

    @property
    def bans(self) -> str:
        """The URL structure for the child route `bans` of `users`."""
        return f"{self._route}/bans"

    @property
    def whitelists(self) -> str:
        """The URL structure for the child route `whitelists` of `users`."""
        return f"{self._route}/whitelists"

    @property
    def reputation(self) -> str:
        return f"{self._route}/rep"
