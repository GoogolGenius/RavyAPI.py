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


def has_permissions(required: str, permissions: list[str]):
    required_list = required.split(".")

    while required_list:
        if ".".join(required_list) in permissions:
            return True
        required_list.pop()

    return False


def with_permission_check(
    required: str,
) -> Callable[[_EndpointF[_EndpointP, _EndpointT]], _EndpointF[_EndpointP, _EndpointT]]:
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
