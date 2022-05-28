from __future__ import annotations

__all__: tuple[str, ...] = ("Paths",)

from ..const import BASE_URL


class Paths:
    """A base class for all Ravy API URL route paths."""

    @property
    def base(self) -> str:
        """The base URL for the Ravy API."""
        return BASE_URL

    @property
    def users(self) -> Users:
        """Route paths for the main `users` endpoint."""
        return Users()

    @property
    def urls(self) -> URLs:
        """Route paths for the main `urls` endpoint."""
        return URLs()

    @property
    def tokens(self) -> Tokens:
        """Route paths for the main `tokens` endpoint."""
        return Tokens()

    @property
    def guilds(self) -> Guilds:
        """Route paths for the main `guilds` endpoint."""
        return Guilds()


class Users:
    """A class containing route paths for the `users` main endpoint."""

    _ENDPOINT_URL = "/users"

    def user(self, id: int) -> str:
        """The URL structure for the `users` main parent endpoint.

        Parameters
        ----------
        id : int
            The user's Discord ID.
        """
        return self._ENDPOINT_URL + f"/{id}"

    def pronouns(self, id: int) -> str:
        """The URL strcture for the child endpoint `pronouns` of `users`.

        Parameters
        ----------
        id : int
            The user's Discord ID.
        """
        return self.user(id) + "/pronouns"

    def bans(self, id: int) -> str:
        """The URL structure for the child endpoint `bans` of `users`.

        Parameters
        ----------
        id : int
            The user's Discord ID.
        """
        return self.user(id) + "/bans"

    def whitelists(self, id: int) -> str:
        """The URL structure for the child endpoint `whitelists` of `users`.

        Parameters
        ----------
        id : int
            The user's Discord ID.
        """
        return self.user(id) + "/whitelists"

    def reputation(self, id: int) -> str:
        return self.user(id) + "/rep"


class URLs:
    """A class containing route paths for the `urls` main endpoint."""

    _ENDPOINT_URL = "/urls"

    def url(self, url: str) -> str:
        """The URL structure for the `urls` main parent endpoint.

        Parameters
        ----------
        url : str
            The URL (encoded) to analyze.
        """
        return self._ENDPOINT_URL + f"/{url}"


class Tokens:
    """A class containing route paths for the `tokens` main endpoint."""

    _ENDPOINT_URL = "/tokens"

    # Does this make sense as a property or function?
    def current(self) -> str:
        """The URL structure for the `tokens` main parent endpoint.

        This is the current token used.
        """
        return self._ENDPOINT_URL + "/@current"


class Guilds:
    """A class containing route paths for the `guilds` main endpoint."""

    _ENDPOINT_URL = "/guilds"

    def guild(self, id: int) -> str:
        """The URL structure for the `guilds` main parent endpoint.

        Parameters
        ----------
        id : int
            The guild's Discord ID.
        """
        return self._ENDPOINT_URL + f"/{id}"
