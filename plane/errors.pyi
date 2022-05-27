from _typeshed import Incomplete

class HTTPException(Exception):
    status: Incomplete
    exc_info: Incomplete
    def __init__(self, status: int, exc_message: str) -> None: ...
