# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
"""Implementations for the ``users`` endpoint."""

from __future__ import annotations

__all__: tuple[str, ...] = ("Users",)

from plane.api.models import (
    GetUserResponse,
    GetPronounsResponse,
    GetBansResponse,
    GetWhitelistsResponse,
    GetReputationResponse,
    BanEntryRequest,
)
from plane.http import HTTPAwareEndpoint
from plane.utils import with_permission_check


class Users(HTTPAwareEndpoint):
    """A class with implementations for the ``users`` endpoint.

    Methods
    -------
    get_user(user_id: int) -> GetUserResponse
        TODO
    get_pronouns(user_id: int) -> GetPronounsResponse
        TODO
    get_bans(user_id: int) -> GetBansResponse
        TODO
    add_ban(user_id: int, ban_entry: BanEntryRequest) -> None
        TODO
    get_whitelists(user_id: int) -> GetWhitelistsResponse
        TODO
    get_reputation(user_id: int) -> GetReputationResponse
        TODO
    """

    __slots__: tuple[str, ...] = ()

    @with_permission_check("users")
    async def get_user(self: HTTPAwareEndpoint, user_id: int) -> GetUserResponse:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetUserResponse(
            await self._http.get(self._http.paths.users(user_id).route)
        )

    @with_permission_check("users.pronouns")
    async def get_pronouns(
        self: HTTPAwareEndpoint, user_id: int
    ) -> GetPronounsResponse:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetPronounsResponse(
            await self._http.get(self._http.paths.users(user_id).pronouns)
        )

    @with_permission_check("users.bans")
    async def get_bans(self: HTTPAwareEndpoint, user_id: int) -> GetBansResponse:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetBansResponse(
            await self._http.get(self._http.paths.users(user_id).bans)
        )

    @with_permission_check("admin.bans")
    async def add_ban(
        self: HTTPAwareEndpoint,
        user_id: int,
        *,
        provider: str,
        reason: str,
        moderator: int,
        reason_key: str | None = None,
    ) -> None:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        if not isinstance(provider, str):
            raise TypeError('Parameter "provider" must be of type "str"')

        if not provider:
            raise ValueError('Parameter "provider" must not be empty')  # TODO: Ask Ravy

        if not isinstance(reason, str):
            raise TypeError('Parameter "reason" must be of type "str"')

        if not reason:
            raise ValueError('Parameter "reason" must not be empty')  # TODO: Ask Ravy

        if not isinstance(moderator, int):
            raise TypeError('Parameter "moderator" must be of type "int"')

        if reason_key is not None and not isinstance(reason_key, str):
            raise TypeError('Parameter "reason_key" must be of type "str"')

        if reason_key is not None and not reason_key:
            raise ValueError('Parameter "reason_key" must not be empty')

        await self._http.post(
            self._http.paths.users(user_id).bans,
            json=BanEntryRequest(provider, reason, moderator, reason_key).to_json(),
        )

    @with_permission_check("users.whitelists")
    async def get_whitelists(
        self: HTTPAwareEndpoint, user_id: int
    ) -> GetWhitelistsResponse:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetWhitelistsResponse(
            await self._http.get(self._http.paths.users(user_id).whitelists)
        )

    @with_permission_check("users.rep")
    async def get_reputation(
        self: HTTPAwareEndpoint, user_id: int
    ) -> GetReputationResponse:
        """TODO"""
        if not isinstance(user_id, int):
            raise TypeError('Parameter "user_id" must be of type "int"')

        return GetReputationResponse(
            await self._http.get(self._http.paths.users(user_id).reputation)
        )
