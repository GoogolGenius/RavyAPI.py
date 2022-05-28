# WIP
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
    pronouns: str
        The user's pronouns.
    trust: Trust
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

    def __init__(self, data: dict[Any, Any]) -> None:
        self.pronouns: str = data["pronouns"]
        self.trust = Trust(data["trust"])
        self.whitelists = WhitelistEntry(data["whitelists"])
        self.bans = BanEntry(data["bans"])
        self.rep = ReputationEntry(data["rep"])
        self.sentinel = SentinelEntry(data["sentinel"])


class GetPronounsResponse:
    """The pronouns data model.

    Attributes
    ----------
    pronouns: str
        The user's pronouns.
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.pronouns: str = data["pronouns"]


class GetBansResponse:
    """The bans data model.

    Attributes
    ----------
    trust: Trust
        The trust model of the user (limited).
    bans : list[BanEntry]
        A list of ban entry models for the user.
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.trust = Trust(data["trust"])
        self.bans = [BanEntry(ban) for ban in data["bans"]]


class GetWhitelistsResponse:
    """The whitelists data model.

    Attributes
    ----------
    whitelists: list[WhitelistEntry]
        A list of whitelist entry models.
    trust: Trust
        The trust model of the user (limited).
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.whitelists = [
            WhitelistEntry(whitelist) for whitelist in data["whitelists"]
        ]
        self.trust = Trust(data["trust"])


class GetReputationResponse:
    """The reputation data model.

    Attributes
    ----------
    rep: list[ReputationEntry]
        A list of reputation entry models.
    trust: Trust
        The trust model of the user (limited).
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.rep = [ReputationEntry(rep) for rep in data["rep"]]
        self.trust = Trust(data["trust"])


class Trust:
    """The trust data model.

    Attributes
    ----------
    level : int
        From 0-6, higher is better, default is 3.
    label : str
        What the number means.
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.level: int = data["level"]
        self.label: str = data["label"]


class WhitelistEntry:
    """The whitelist entry data model.

    Attributes
    ----------
    provider : str
        Source for where the user is whitelisted.
    reason : str
        Why the user is whitelisted, usually STAFF.
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.provider: str = data["provider"]
        self.reason: str = data["reason"]


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

    def __init__(self, data: dict[Any, Any]) -> None:
        self.provider: str = data["provider"]
        self.reason: str = data["reason"]
        self.reason_key: str | None = data["reason_key"]
        self.moderator: str = data["moderator"]


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

    def __init__(self, data: dict[Any, Any]) -> None:
        self.provider: str = data["provider"]
        self.score: float = data["score"]
        self.upvotes: int | None = data["upvotes"]
        self.downvotes: int | None = data["downvotes"]


class SentinelEntry:
    """The sentinel entry data model.

    Attributes
    ----------
    verified : bool
        Whether this user has linked their account to sentinel
    id : str
        Internal ID for debug purposes
    """

    def __init__(self, data: dict[Any, Any]) -> None:
        self.verified: bool = data["verified"]
        self.id: int = int(data["id"])
