# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""Constants used by library API wrapper."""

from __future__ import annotations

__all__: tuple[str, ...] = (
    "BASE_URL",
    "RAVY_TOKEN_REGEX",
    "KSOFT_TOKEN_REGEX",
    "USER_AGENT",
)

import platform

import aiohttp
from typing_extensions import Final

from plane._about import __author__, __repository__, __version__

BASE_URL: Final[str] = "https://ravy.org/api/v1"
"""The base URL for the Ravy API."""

RAVY_TOKEN_REGEX: Final[str] = r"[A-Za-z0-9_-]{24}\.[0-9a-f]{64}"
"""The regex for a Ravy token."""

KSOFT_TOKEN_REGEX: Final[str] = r"[0-9a-f]{40}"
"""The regex for a KSoft token."""

# Totally not copied from Hikari lol
USER_AGENT: Final[str] = (
    f"plane ({__repository__}, {__version__}) {__author__} "
    f"aiohttp/{aiohttp.__version__} "
    f"{platform.python_implementation()}/{platform.python_version()} "
    f"{platform.system()} {platform.architecture()[0]}"
)
"""The user agent for requests."""
