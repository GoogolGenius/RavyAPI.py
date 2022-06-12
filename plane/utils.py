# Copyright 2022-Present GoogleGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import annotations

__all__: tuple[str, ...] = ("with_permission_check",)

from functools import wraps
from typing import Any, Callable, Coroutine, TYPE_CHECKING, TypeVar
from typing_extensions import Concatenate, ParamSpec, TypeAlias

from plane.api.errors import AccessException

if TYPE_CHECKING:
    from plane.http import HTTPAwareEndpoint

    _EndpointP = ParamSpec("_EndpointP")
    _EndpointT = TypeVar("_EndpointT")
    _EndpointF: TypeAlias = Callable[
        Concatenate[HTTPAwareEndpoint, _EndpointP], Coroutine[_EndpointT, Any, Any]
    ]


def has_permissions(required: str, permissions: list[str]) -> bool:
    """Process the current token permissions to match against the required permissions.

    !!! warning
        This is an internal function and should not be used unless you know what you are doing.

    Parameters
    ----------
    required : str
        The required permissions.
    permissions : list[str]
        The permissions of the current token to match against.

    Returns
    -------
    bool
        Whether or not the token has the required permissions.
    """
    required_list = required.split(".")

    while required_list:
        if ".".join(required_list) in permissions:
            return True
        required_list.pop()

    return False


def with_permission_check(
    required: str,
) -> Callable[[_EndpointF[_EndpointP, _EndpointT]], _EndpointF[_EndpointP, _EndpointT]]:
    """Decorate an instance method of an `HTTPAwareEndpoint` to validate permissions.

    !!! warning
        This is an internal decorator and should not be used unless you know what you are doing."""

    def decorator(
        function: _EndpointF[_EndpointP, _EndpointT]
    ) -> _EndpointF[_EndpointP, _EndpointT]:
        @wraps(function)
        async def wrapper(
            self: HTTPAwareEndpoint, *args: _EndpointP.args, **kwargs: _EndpointP.kwargs
        ) -> Coroutine[_EndpointT, Any, Any]:
            if not has_permissions(required, self._http.permissions):  # type: ignore
                raise AccessException(required)
            return await function(self, *args, **kwargs)

        return wrapper

    return decorator
