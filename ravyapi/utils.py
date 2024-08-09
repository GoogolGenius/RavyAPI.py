# Copyright 2022-Present GoogolGenius
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
"""Internal utilities for the API wrapper."""

from __future__ import annotations

__all__: tuple[str, ...] = ("with_permission_check",)

from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Coroutine, TypeVar

from typing import Concatenate, ParamSpec, TypeAlias

from ravyapi.api.errors import AccessError

if TYPE_CHECKING:
    from ravyapi.http import HTTPAwareEndpoint

    _EndpointP = ParamSpec("_EndpointP")
    _EndpointT = TypeVar("_EndpointT")
    _EndpointR = TypeVar("_EndpointR")
    _EndpointF: TypeAlias = Callable[
        Concatenate[HTTPAwareEndpoint, _EndpointP],
        Coroutine[_EndpointT, Any, _EndpointR],
    ]


def has_permissions(required: str, permissions: list[str]) -> bool:
    """Check whether the required permissions match a list of permissions.

    Parameters
    ----------
    required : str
        The required permissions.
    permissions : list[str]
        The list of permissions.

    Returns
    -------
    bool
        Whether the permissions match.
    """
    required_list = required.split(".")

    while required_list:
        if ".".join(required_list) in permissions:
            return True
        required_list.pop()

    return False


def with_permission_check(
    required: str,
) -> Callable[
    [_EndpointF[_EndpointP, _EndpointT, _EndpointR]],
    _EndpointF[_EndpointP, _EndpointT, _EndpointR],
]:
    """Decorate an instance method of `ravyapi.http.HTTPAwareEndpoint` to validate the required permissions.

    !!! warning
        This is an internal function and should not be used unless you know what you are doing.

    Parameters
    ----------
    required : str
        The required permissions.

    Returns
    -------
    Callable[[_EndpointF[_EndpointP, _EndpointT]], _EndpointF[_EndpointP, _EndpointT]]
    """

    def decorator(
        function: _EndpointF[_EndpointP, _EndpointT, _EndpointR]
    ) -> _EndpointF[_EndpointP, _EndpointT, _EndpointR]:
        @wraps(function)
        async def wrapper(
            self: HTTPAwareEndpoint, *args: _EndpointP.args, **kwargs: _EndpointP.kwargs
        ) -> _EndpointR:
            await self._http.get_permissions()

            if self._http.permissions is None:
                raise AssertionError(
                    'Permissions is "None"; were permissions not yet fetched or unexpectedly modified?'
                )

            if not has_permissions(required, self._http.permissions):
                raise AccessError(required)

            return await function(self, *args, **kwargs)

        return wrapper

    return decorator
