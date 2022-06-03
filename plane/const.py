from __future__ import annotations

__all__: tuple[str, ...] = ("BASE_URL", "RAVY_TOKEN_REGEX", "KSOFT_TOKEN_REGEX")

from typing_extensions import Final

BASE_URL: Final[str] = "https://ravy.org/api/v1"
"""The base URL of the Ravy API."""

RAVY_TOKEN_REGEX: Final[str] = r"[A-Za-z0-9_-]{24}\.[0-9a-f]{64}"
"""The regex for validating a Ravy token."""

KSOFT_TOKEN_REGEX: Final[str] = r"[0-9a-f]{40}"
"""The regex for validating a KSoft token."""

NULL: Final[str] = "\x00"
"""Null byte."""
