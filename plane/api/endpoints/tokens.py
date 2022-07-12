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
"""Implementations for the `tokens` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)

from plane.api.models import GetTokenResponse
from plane.http import HTTPAwareEndpoint


class Tokens(HTTPAwareEndpoint):
    """A class with implementations for the `tokens` endpoint."""

    __slots__: tuple[str, ...] = ()

    async def get_token(self: HTTPAwareEndpoint) -> GetTokenResponse:
        """Get current token information.

        Returns
        -------
        GetTokenResponse
            A model response from `plane.api.endpoints.tokens.Tokens.get_token`.
            Located as `plane.api.models.tokens.GetTokenResponse`.
        """
        return GetTokenResponse(await self._http.get(self._http.paths.tokens.route))
