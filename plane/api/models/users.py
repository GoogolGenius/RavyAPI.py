# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""API models for the ``users`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = (
    "GetUserResponse",
    "GetPronounsResponse",
    "GetBansResponse",
    "GetWhitelistsResponse",
    "GetReputationResponse",
    "WhitelistEntry",
    "ReputationEntry",
    "SentinelEntry",
)

from typing import Any

from plane.api.models.generic import Trust, BanEntryResponse


class GetUserResponse:
    """A model response from :func:`plane.api.endpoints.users.Users.get_user`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    pronouns : str
        The user's pronouns.
    trust : Trust
        The user's :class:`plane.api.models.generic.trust.Trust` trust model.
    whitelists : WhitelistEntry
        The user's :class:`plane.api.models.users.WhitelistEntry` whitelist model.
    bans : BanEntryResponse
        The user's :class:`plane.api.models.generic.ban_entry.BanEntryResponse` ban model.
    rep : ReputationEntry
        The user's :class:`plane.api.models.users.ReputationEntry` reputation model.
    sentinel : SentinelEntry
        The user's :class:`plane.api.models.users.SentinelEntry` sentinel model.
    """

    __slots__: tuple[str, ...] = (
        "_data",
        "_pronouns",
        "_trust",
        "_whitelists",
        "_bans",
        "_rep",
        "_sentinel",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._pronouns: str = data["pronouns"]
        self._trust = Trust(data["trust"])
        self._whitelists = WhitelistEntry(data["whitelists"])
        self._bans = BanEntryResponse(data["bans"])
        self._rep = ReputationEntry(data["rep"])
        self._sentinel = SentinelEntry(data["sentinel"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def pronouns(self) -> str:
        """The user's pronouns."""
        return self._pronouns

    @property
    def trust(self) -> Trust:
        """The user's :class:`plane.api.models.generic.trust.Trust` trust model."""
        return self._trust

    @property
    def whitelists(self) -> WhitelistEntry:
        """The user's :class:`plane.api.models.users.WhitelistEntry` whitelist model."""
        return self._whitelists

    @property
    def bans(self) -> BanEntryResponse:
        """The user's :class:`plane.api.models.generic.ban_entry.BanEntryResponse` ban model."""
        return self._bans

    @property
    def rep(self) -> ReputationEntry:
        """The user's :class:`plane.api.models.users.ReputationEntry` reputation model."""
        return self._rep

    @property
    def sentinel(self) -> SentinelEntry:
        """The user's :class:`plane.api.models.users.SentinelEntry` sentinel model."""
        return self._sentinel


class GetPronounsResponse:
    """A model response from :func:`plane.api.endpoints.users.Users.get_pronouns`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    pronouns : str
        The user's pronouns.
    """

    __slots__: tuple[str, ...] = ("_data", "_pronouns")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._pronouns: str = data["pronouns"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def pronouns(self) -> str:
        """The user's pronouns."""
        return self._pronouns


class GetBansResponse:
    """A model response from :func:`plane.api.endpoints.users.Users.get_bans`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    trust : Trust
        The user's :class:`plane.api.models.generic.trust.Trust` trust model.
    bans : list[BanEntryResponse]
        A list of the user's :class:`plane.api.models.generic.ban_entry.BanEntryResponse` ban models.
    """

    __slots__: tuple[str, ...] = ("_data", "_trust", "_bans")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._trust = Trust(data["trust"])
        self._bans = [BanEntryResponse(ban) for ban in data["bans"]]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def trust(self) -> Trust:
        """The user's :class:`plane.api.models.generic.trust.Trust` trust model."""
        return self._trust

    @property
    def bans(self) -> list[BanEntryResponse]:
        """A list of the user's :class:`plane.api.models.generic.ban_entry.BanEntryResponse` ban models."""
        return self._bans


class GetWhitelistsResponse:
    """A model response from :func:`plane.api.endpoints.users.Users.get_whitelists`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    whitelists : list[WhitelistEntry]
        A list of the user's :class:`plane.api.models.users.WhitelistEntry` whitelist models.
    trust : Trust
        The user's :class:`plane.api.models.generic.trust.Trust` trust model.
    """

    __slots__: tuple[str, ...] = ("_data", "_whitelists", "_trust")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._whitelists = [
            WhitelistEntry(whitelist) for whitelist in data["whitelists"]
        ]
        self._trust = Trust(data["trust"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def whitelists(self) -> list[WhitelistEntry]:
        """A list of the user's :class:`plane.api.models.users.WhitelistEntry` whitelist models."""
        return self._whitelists

    @property
    def trust(self) -> Trust:
        """The user's :class:`plane.api.models.generic.trust.Trust` trust model."""
        return self._trust


class GetReputationResponse:
    """A model response from :func:`plane.api.endpoints.users.Users.get_reputation`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    rep : ReputationEntry
        The user's :class:`plane.api.models.users.ReputationEntry` reputation model.
    trust : Trust
        The user's :class:`plane.api.models.generic.trust.Trust` trust model.
    """

    __slots__: tuple[str, ...] = ("_data", "_rep", "_trust")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._rep = [ReputationEntry(rep) for rep in data["rep"]]
        self._trust = Trust(data["trust"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def rep(self) -> list[ReputationEntry]:
        """A list of the user's :class:`plane.api.models.users.ReputationEntry` reputation models."""
        return self._rep

    @property
    def trust(self) -> Trust:
        """The user's :class:`plane.api.models.generic.trust.Trust` trust model."""
        return self._trust


class WhitelistEntry:
    """A model for a user's whitelist entry.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    provider : str
        TODO
    reason : str
        TODO
    """

    __slots__: tuple[str, ...] = ("_data", "_provider", "_reason")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def provider(self) -> str:
        """TODO"""
        return self._provider

    @property
    def reason(self) -> str:
        """TODO"""
        return self._reason


class ReputationEntry:
    """A model for a user's reputation entry.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    provider : str
        TODO
    score : float
        TODO
    upvotes : int | None
        TODO
    downvotes : int | None
        TODO
    """

    __slots__: tuple[str, ...] = (
        "_data",
        "_provider",
        "_score",
        "_upvotes",
        "_downvotes",
    )

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._provider: str = data["provider"]
        self._score: float = data["score"]
        self._upvotes: int | None = data.get("upvotes")
        self._downvotes: int | None = data.get("downvotes")

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def provider(self) -> str:
        """TODO"""
        return self._provider

    @property
    def score(self) -> float:
        """TODO"""
        return self._score

    @property
    def upvotes(self) -> int | None:
        """TODO"""
        return self._upvotes

    @property
    def downvotes(self) -> int | None:
        """TODO"""
        return self._downvotes


class SentinelEntry:
    """A model for a user's sentinel entry.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    verified : bool
        TODO
    internal_id : str
        TODO
    """

    __slots__: tuple[str, ...] = ("_data", "_verified", "_internal_id")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._verified: bool = data["verified"]
        self._internal_id: str = str(data["id"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def verified(self) -> bool:
        """TODO"""
        return self._verified

    @property
    def internal_id(self) -> str:
        """TODO"""
        return self._internal_id
