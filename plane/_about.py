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
"""Metadata information about the package."""

from __future__ import annotations

__all__: tuple[str, ...] = (
    "__author__",
    "__repository__",
    "__copyright__",
    "__license__",
    "__version__",
    "__maintainer__",
    "__email__",
    "__status__",
)

from typing_extensions import Final

__author__: Final[str] = "GoogleGenius"
__repository__: Final[str] = "https://github.com/GoogleGenius/plane"
__copyright__: Final[str] = "Copyright 2022-Present GoogleGenius"
__license__: Final[str] = "GNU GPLv3"
__version__: Final[str] = "0.1.0a"
__maintainer__: Final[str] = "GoogleGenius"
__email__: Final[str] = "erich.nguyen@outlook.com"
__status__: Final[str] = "Planning"
