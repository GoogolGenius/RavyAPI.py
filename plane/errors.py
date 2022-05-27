from __future__ import annotations

__all__: tuple[str, ...] = ("HTTPException",)


class HTTPException(Exception):
    def __init__(self, status: int, exc_message: str):
        self.status: int = status
        self.exc_info: str = exc_message

    def __str__(self) -> str:
        return f"{self.status}\n{self.exc_info}"
