from __future__ import annotations
from typing import Any

__all__: tuple[str, ...] = (
    "GetUserResponse",
    "GetPronounsResponse",
    "GetBansResponse",
    "GetWhitelistsResponse",
    "GetReputationResponse",
    "Trust",
    "WhitelistEntry",
    "BanEntry",
    "ReputationEntry",
    "SentinelEntry",
)


class GetUserResponse:
    """The user data model.

    Attributes
    ----------
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
    """The pronouns data model.

    Attributes
    ----------
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
    """The bans data model.

    Attributes
    ----------
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
    """The whitelists data model.

    Attributes
    ----------
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
    """The reputation data model.

    Attributes
    ----------
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


class Trust:
    """The trust data model.

    Attributes
    ----------
    level : int
        From 0-6, higher is better, default is 3.
    label : str
        What the number means.
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._level: int = data["level"]
        self._label: str = data["label"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def level(self) -> int:
        """From 0-6, higher is better."""
        return self._level

    @property
    def label(self) -> str:
        """What the number means."""
        return self._label


class WhitelistEntry:
    """The whitelist entry data model.

    Attributes
    ----------
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


class BanEntry:
    """The ban entry data model.

    Attributes
    ----------
    provider : str
        Source for where the user is banned.
    reason : str
        Why the user is banned, usually STAFF.
    reason_key : str | None
        Machine-readable version of the reason - only present for providers ravy and dservices
    moderator : str
        User ID of the responsible moderator, usually Discord
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._provider: str = data["provider"]
        self._reason: str = data["reason"]
        self._reason_key: str | None = data["reason_key"]
        self._moderator: str = data["moderator"]

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def provider(self) -> str:
        """Source for where the user is banned."""
        return self._provider

    @property
    def reason(self) -> str:
        """Why the user is banned, usually STAFF."""
        return self._reason

    @property
    def reason_key(self) -> str | None:
        """Machine-readable version of the reason - only present for providers ravy and dservices."""
        return self._reason_key

    @property
    def moderator(self) -> str:
        """User ID of the responsible moderator, usually Discord."""
        return self._moderator


class ReputationEntry:
    """The reputation entry data model.

    Attributes
    ----------
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
        self._upvotes: int | None = data["upvotes"]
        self._downvotes: int | None = data["downvotes"]

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
    id : str
        Internal ID for debug purposes
    """

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data
        self._verified: bool = data["verified"]
        self._id: int = int(data["id"])

    @property
    def data(self) -> dict[str, Any]:
        """The raw JSON data from the API."""
        return self._data

    @property
    def verified(self) -> bool:
        """Whether this user has linked their account to sentinel."""
        return self._verified

    @property
    def id(self) -> int:
        """Internal ID for debug purposes."""
        return self._id
