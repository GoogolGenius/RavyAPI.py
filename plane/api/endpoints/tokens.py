# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("Tokens",)

from plane.api.models import GetTokenResponse
from plane.http import HTTPAwareEndpoint


class Tokens(HTTPAwareEndpoint):
    """The implementation class for requests to the `tokens` route."""

    async def get_token(self: HTTPAwareEndpoint) -> GetTokenResponse:
        """Get current token information.

        Returns
        -------
        GetTokenResponse
            The response from the API.
        """
        return GetTokenResponse(await self._http.get(self._http.paths.tokens.route))
