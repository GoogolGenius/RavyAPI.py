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

from .generic import Trust, BanEntry


class GetUserResponse:
    """The user response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    pronouns : str
        The user's pronouns.
    trust : Trust
        The trust model of the user.
    whitelists : WhitelistEntry
        The whitelist entry model of the user.
    bans : BanEntry
        The ban entry model of the user.
    rep : ReputationEntry
        The reputation entry model of the user.
    sentinel : SentinelEntry
        The sentinel entry model of the user.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._pronouns: str = data["pronouns"]
        self._trust = Trust(data["trust"])
        self._whitelists = WhitelistEntry(data["whitelists"])
        self._bans = BanEntry(data["bans"])
        self._rep = ReputationEntry(data["rep"])
        self._sentinel = SentinelEntry(data["sentinel"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def pronouns(self) -> str:
        """The user's pronouns."""
        return self._pronouns

    @property
    def trust(self) -> Trust:
        """The trust model of the user."""
        return self._trust

    @property
    def whitelists(self) -> WhitelistEntry:
        """The whitelist entry model of the user."""
        return self._whitelists

    @property
    def bans(self) -> BanEntry:
        """The ban entry model of the user."""
        return self._bans

    @property
    def rep(self) -> ReputationEntry:
        """The reputation entry model of the user."""
        return self._rep

    @property
    def sentinel(self) -> SentinelEntry:
        """The sentinel entry model of the user."""
        return self._sentinel


class GetPronounsResponse:
    """The pronouns response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    pronouns: str
        The user's pronouns.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._pronouns: str = data["pronouns"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def pronouns(self) -> str:
        """The user's pronouns."""
        return self._pronouns


class GetBansResponse:
    """The bans response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    trust : Trust
        The trust model of the user (limited).
    bans : list[BanEntry]
        A list of ban entry models for the user.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._trust = Trust(data["trust"])
        self._bans = [BanEntry(ban) for ban in data["bans"]]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def trust(self) -> Trust:
        """The trust model of the user."""
        return self._trust

    @property
    def bans(self) -> list[BanEntry]:
        """A list of ban entry models for the user."""
        return self._bans


class GetWhitelistsResponse:
    """The whitelists response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    whitelists : list[WhitelistEntry]
        A list of whitelist entry models.
    trust : Trust
        The trust model of the user (limited).
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._whitelists = [
            WhitelistEntry(whitelist) for whitelist in data["whitelists"]
        ]
        self._trust = Trust(data["trust"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def whitelists(self) -> list[WhitelistEntry]:
        """A list of whitelist entry models."""
        return self._whitelists

    @property
    def trust(self) -> Trust:
        """The trust model of the user."""
        return self._trust


class GetReputationResponse:
    """The reputation response data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    rep : list[ReputationEntry]
        A list of reputation entry models.
    trust : Trust
        The trust model of the user (limited).
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._rep = [ReputationEntry(rep) for rep in data["rep"]]
        self._trust = Trust(data["trust"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def rep(self) -> list[ReputationEntry]:
        """A list of reputation entry models."""
        return self._rep

    @property
    def trust(self) -> Trust:
        """The trust model of the user."""
        return self._trust


class WhitelistEntry:
    """The whitelist entry data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    provider : str
        Source for where the user is whitelisted.
    reason : str
        Why the user is whitelisted, usually STAFF.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
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
    """The reputation entry data model.

    Attributes
    ----------
    data : dict[str, Any]
        The raw data from the API.
    provider : str
        Source for where the user is banned.
    score : float
        Normalized value (0-1) for reputation of the user, 0.5 is default
    upvotes : int | None
        Amount of upvotes this user has received, optional
    downvotes : int | None
        Amount of downvotes this user has received, optional
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._provider: str = data["provider"]
        self._score: float = data["score"]
        self._upvotes: int | None = data.get("upvotes")
        self._downvotes: int | None = data.get("downvotes")

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for where the user is banned."""
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
    """The sentinel entry data model.

    Attributes
    ----------
    verified : bool
        Whether this user has linked their account to sentinel
    internal_id : str
        Internal ID for debug purposes
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._verified: bool = data["verified"]
        self._internal_id: int = int(data["id"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def verified(self) -> bool:
        """Whether this user has linked their account to sentinel."""
        return self._verified

    @property
    def internal_id(self) -> int:
        """Internal ID for debug purposes."""
        return self._internal_id
        # Need to ask Ravy whether or not this is just the Discord ID
