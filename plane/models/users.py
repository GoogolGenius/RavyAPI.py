# WIP
from __future__ import annotations

__all__: tuple[str, ...] = ()

from dataclasses import dataclass


@dataclass
class GetUser:
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

    pronouns: str
    trust: Trust
    whitelists: WhitelistEntry
    bans: BanEntry
    rep: ReputationEntry
    sentinel: SentinelEntry


@dataclass
class GetPronouns:
    """The pronouns data model.

    Attributes
    ----------
    pronouns: str
        The user's pronouns.
    """

    pronouns: str


@dataclass
class GetBans:
    """The bans data model.

    Attributes
    ----------
    trust: Trust
        The trust model of the user (limited).
    bans : list[BanEntry]
        A list of ban entry models for the user.
    """

    trust: Trust
    bans: list[BanEntry]


@dataclass
class GetWhitelists:
    """The whitelists data model.

    Attributes
    ----------
    whitelists: list[WhitelistEntry]
        A list of whitelist entry models.
    trust: Trust
        The trust model of the user (limited).
    """

    whitelists: list[WhitelistEntry]
    trust: Trust


@dataclass
class GetReputation:
    """The reputation data model.

    Attributes
    ----------
    rep: list[ReputationEntry]
        A list of reputation entry models.
    trust: Trust
        The trust model of the user (limited).
    """

    rep: list[ReputationEntry]
    trust: Trust


@dataclass
class Trust:
    """The trust data model.

    Attributes
    ----------
    level : int
        From 0-6, higher is better, default is 3.
    label : str
        What the number means.
    """

    level: int
    label: str


@dataclass
class WhitelistEntry:
    """The whitelist entry data model.

    Attributes
    ----------
    provider : str
        Source for where the user is whitelisted.
    reason : str
        Why the user is whitelisted, usually STAFF.
    """

    provider: str
    reason: str


@dataclass
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

    provider: str
    reason: str
    reason_key: str | None
    moderator: str


@dataclass
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

    provider: str
    score: float
    upvotes: int | None
    downvotes: int | None


@dataclass
class SentinelEntry:
    """The sentinel entry data model.

    Attributes
    ----------
    verified : bool
        Whether this user has linked their account to sentinel
    id : str
        Internal ID for debug purposes
    """

    verified: bool
    id: str
