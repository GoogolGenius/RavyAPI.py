from __future__ import annotations

__all__: tuple[str, ...] = ("with_permission_check",)

import functools

from typing import Any, Callable, Coroutine

from .api.errors import AccessException


def has_permissions(required: str, perms: list[str]):
    required_list = required.split(".")

    while required_list:
        if ".".join(required_list) in perms:
            return True
        required_list.pop()

    return False


def with_permission_check(
    required: str,
) -> Callable[..., Callable[..., Coroutine[Any, Any, Any]]]:
    def decorator(
        function: Callable[..., Coroutine[Any, Any, Any]]
    ) -> Callable[..., Coroutine[Any, Any, Any]]:
        @functools.wraps(function)
        async def wrapper(
            self: Any, *args: tuple[Any, ...], **kwargs: dict[str, Any]
        ) -> Coroutine[Any, Any, Any]:
            if not has_permissions(required, self._http.permissions):
                raise AccessException(required)
            return await function(self, *args, **kwargs)

        return wrapper

    return decorator
