# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

import urllib.parse

from plane.api.models import GetWebsiteResponse, EditWebsiteRequest
from plane.const import NULL
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class URLs(HTTPAwareEndpoint):
    """The implementation class for requests to the `urls` route."""

    @with_permission_check("urls.cached")
    async def get_website(
        self: HTTPAwareEndpoint,
        url: str,
        *,
        author: int | None = None,
        phisherman_user: int | None = None,
    ) -> GetWebsiteResponse:
        """Get website information.

        Parameters
        ----------
        url : str
            The url-encoded url to look up.
        author : int | None
            Optional, the user that posted the message containing this URL (for auto banning, requires "admin.users").
            The API ignores this if "admin.users" is not granted permission.
        phisherman_user : int | None
            Optional, required if passing phisherman_token, Discord user ID of the token owner.

        Returns
        -------
        GetWebsiteResponse
            The response from the API.
        """
        if not isinstance(url, str):
            raise ValueError('Parameter "url" must be of "str" or derivative type')

        if author is not None and not isinstance(author, int):
            raise ValueError('Parameter "author" must be of "int" or derivative type')

        if phisherman_user is not None and not isinstance(phisherman_user, int):
            raise ValueError(
                'Parameter "phisherman_user" must be of "int" or derivative type'
            )

        if self._http.phisherman_token is None and phisherman_user:
            raise ValueError("Phisherman token required if phisherman user is set.")

        if self._http.phisherman_token is not None and not phisherman_user:
            raise ValueError("Phisherman user required if phisherman token is set.")

        return GetWebsiteResponse(
            await self._http.get(
                self._http.paths.urls.route,
                params={
                    "url": url,
                    "author": author or NULL,
                    "phisherman_token": self._http.phisherman_token or NULL,
                    "phisherman_user": phisherman_user or NULL,
                },
            )
        )

    @with_permission_check("admin.urls")
    async def edit_website(
        self: HTTPAwareEndpoint,
        url: str,
        *,
        is_fraudulent: bool,
        message: str,
        encode: bool = True,
    ) -> None:
        """Edit website information.

        !!! note
            This endpoint is only available to administrators; however, documented nevertheless.

        Parameters
        ----------
        url : str
            the url-encoded url to set data for
        is_fraudulent : bool
            Whether the website is fraudulent or not.
        message : str
            The message to display to the user.
        """
        if not isinstance(url, str):
            raise ValueError('Parameter "url" must be of "str" or derivative type')

        if not isinstance(is_fraudulent, bool):
            raise ValueError(
                'Parameter "is_fraudulent" must be of "bool" or derivative type'
            )

        if not isinstance(message, str):
            raise ValueError('Parameter "message" must be of "str" or derivative type')

        if not isinstance(encode, bool):
            raise ValueError('Parameter "encode" must be of "bool" or derivative type')

        if encode:
            message = urllib.parse.quote_plus(message)

        await self._http.post(
            f"{self._http.paths.urls.route}/{url}",
            data=EditWebsiteRequest(is_fraudulent, message).from_model(),
        )
