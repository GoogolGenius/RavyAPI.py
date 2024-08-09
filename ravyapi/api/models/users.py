# Copyright 2022-Present GoogolGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API models for the `users` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = (
    "GetBansResponse",
    "GetPronounsResponse",
    "GetReputationResponse",
    "GetUserResponse",
    "GetWhitelistsResponse",
    "ReputationEntry",
    "SentinelEntry",
    "WhitelistEntry",
)

from typing import Any

from ravyapi.api.models.generic import BanEntryResponse, Trust


class GetUserResponse:
    """A model response from `ravyapi.api.endpoints.users.Users.get_user`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    pronouns : str
        The user's pronouns.
    trust : Trust
        The user's `ravyapi.api.models.generic.trust.Trust` trust model.
    whitelists : list[WhitelistEntry]
        A list of the user's `ravyapi.api.models.users.WhitelistEntry` whitelist models.
    bans : list[BanEntryResponse]
        A list of the user's `ravyapi.api.models.generic.ban_entry.BanEntryResponse` ban models.
    rep : list[ReputationEntry]
        A list of the user's `ravyapi.api.models.users.ReputationEntry` reputation models.
    sentinel : SentinelEntry
        The user's `ravyapi.api.models.users.SentinelEntry` sentinel model.
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
        self._trust: Trust = Trust(data["trust"])
        self._whitelists: list[WhitelistEntry] = [
            WhitelistEntry(whitelist) for whitelist in data["whitelists"]
        ]
        self._bans: list[BanEntryResponse] = [
            BanEntryResponse(ban) for ban in data["bans"]
        ]
        self._rep: list[ReputationEntry] = [ReputationEntry(rep) for rep in data["rep"]]
        self._sentinel: SentinelEntry = SentinelEntry(data["sentinel"])

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(pronouns={self.pronouns!r}, trust={self.trust!r}, "
            f"whitelists={self.whitelists!r}, bans={self.bans!r}, "
            f"rep={self.rep!r}, sentinel={self.sentinel!r})"
        )

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
        """The user's `ravyapi.api.models.generic.trust.Trust` trust model."""
        return self._trust

    @property
    def whitelists(self) -> list[WhitelistEntry]:
        """A list of the user's `ravyapi.api.models.users.WhitelistEntry` whitelist models."""
        return self._whitelists

    @property
    def bans(self) -> list[BanEntryResponse]:
        """A list of the user's `ravyapi.api.models.generic.ban_entry.BanEntryResponse` ban models."""
        return self._bans

    @property
    def rep(self) -> list[ReputationEntry]:
        """A list of the user's `ravyapi.api.models.users.ReputationEntry` reputation models."""
        return self._rep

    @property
    def sentinel(self) -> SentinelEntry:
        """The user's `ravyapi.api.models.users.SentinelEntry` sentinel model."""
        return self._sentinel


class GetPronounsResponse:
    """A model response from `ravyapi.api.endpoints.users.Users.get_pronouns`.

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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(pronouns={self.pronouns!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def pronouns(self) -> str:
        """The user's pronouns."""
        return self._pronouns


class GetBansResponse:
    """A model response from `ravyapi.api.endpoints.users.Users.get_bans`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    trust : Trust
        The user's `ravyapi.api.models.generic.trust.Trust` trust model.
    bans : list[BanEntryResponse]
        A list of the user's `ravyapi.api.models.generic.ban_entry.BanEntryResponse` ban models.
    """

    __slots__: tuple[str, ...] = ("_data", "_trust", "_bans")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._trust = Trust(data["trust"])
        self._bans = [BanEntryResponse(ban) for ban in data["bans"]]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(trust={self.trust!r}, bans={self.bans!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def trust(self) -> Trust:
        """The user's `ravyapi.api.models.generic.trust.Trust` trust model."""
        return self._trust

    @property
    def bans(self) -> list[BanEntryResponse]:
        """A list of the user's `ravyapi.api.models.generic.ban_entry.BanEntryResponse` ban models."""
        return self._bans


class GetWhitelistsResponse:
    """A model response from `ravyapi.api.endpoints.users.Users.get_whitelists`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    whitelists : list[WhitelistEntry]
        A list of the user's `ravyapi.api.models.users.WhitelistEntry` whitelist models.
    trust : Trust
        The user's `ravyapi.api.models.generic.trust.Trust` trust model.
    """

    __slots__: tuple[str, ...] = ("_data", "_whitelists", "_trust")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._whitelists = [
            WhitelistEntry(whitelist) for whitelist in data["whitelists"]
        ]
        self._trust = Trust(data["trust"])

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(whitelists={self.whitelists!r}, trust={self.trust!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def whitelists(self) -> list[WhitelistEntry]:
        """A list of the user's `ravyapi.api.models.users.WhitelistEntry` whitelist models."""
        return self._whitelists

    @property
    def trust(self) -> Trust:
        """The user's `ravyapi.api.models.generic.trust.Trust` trust model."""
        return self._trust


class GetReputationResponse:
    """A model response from `ravyapi.api.endpoints.users.Users.get_reputation`.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    rep : list[ReputationEntry]
        A list of the user's `ravyapi.api.models.users.ReputationEntry` reputation models.
    trust : Trust
        The user's `ravyapi.api.models.generic.trust.Trust` trust model.
    """

    __slots__: tuple[str, ...] = ("_data", "_rep", "_trust")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._rep = [ReputationEntry(rep) for rep in data["rep"]]
        self._trust = Trust(data["trust"])

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(rep={self.rep!r}, trust={self.trust!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def rep(self) -> list[ReputationEntry]:
        """A list of the user's `ravyapi.api.models.users.ReputationEntry` reputation models."""
        return self._rep

    @property
    def trust(self) -> Trust:
        """The user's `ravyapi.api.models.generic.trust.Trust` trust model."""
        return self._trust


class WhitelistEntry:
    """A model for a user's whitelist entry.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    provider : str
        Source for where the user is whitelisted.
    reason : str
        Why the user is whitelisted, usually STAFF.
    """

    __slots__: tuple[str, ...] = ("_data", "_provider", "_reason")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(provider={self.provider!r}, reason={self.reason!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for where the user is whitelisted."""
        return self._provider

    @property
    def reason(self) -> str:
        """Why the user is whitelisted, usually STAFF."""
        return self._reason


class ReputationEntry:
    """A model for a user's reputation entry.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    provider : str
        Source for the reputation data.
    score : float
        Normalized value (0-1) for reputation of the user, 0.5 is default.
    upvotes : int | None
        Amount of upvotes this user has received, optional.
    downvotes : int | None
        Amount of downvotes this user has received, optional.
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

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(provider={self.provider!r}, score={self.score!r}, "
            f"upvotes={self.upvotes!r}, downvotes={self.downvotes!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for the reputation data."""
        return self._provider

    @property
    def score(self) -> float:
        """Normalized value (0-1) for reputation of the user, 0.5 is default."""
        return self._score

    @property
    def upvotes(self) -> int | None:
        """Amount of upvotes this user has received, optional."""
        return self._upvotes

    @property
    def downvotes(self) -> int | None:
        """Amount of downvotes this user has received, optional."""
        return self._downvotes


class SentinelEntry:
    """A model for a user's sentinel entry.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data returned from the Ravy API.
    verified : bool
        Whether this user has linked their account to sentinel.
    internal_id : str
        Internal ID for debug purposes.
    """

    __slots__: tuple[str, ...] = ("_data", "_verified", "_internal_id")

    def __init__(self, data: dict[str, Any]) -> None:
        self._data: dict[str, Any] = data
        self._verified: bool = data["verified"]
        self._internal_id: str = str(data["id"])

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}"
            f"(verified={self.verified!r}, internal_id={self.internal_id!r})"
        )

    @property
    def data(self) -> dict[str, Any]:
        """The raw data returned from the Ravy API."""
        return self._data

    @property
    def verified(self) -> bool:
        """Whether this user has linked their account to sentinel."""
        return self._verified

    @property
    def internal_id(self) -> str:
        """Internal ID for debug purposes."""
        return self._internal_id
