# Copyright 2022-Present GoogleGenius
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
#
# Copyright (c) 2020 Nekokatt
# Copyright (c) 2021-present davfsa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
