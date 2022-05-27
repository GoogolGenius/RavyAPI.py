from ..http import HTTPClient
from ..routes import Routes
from typing import Any

class URLs:
    def __init__(self, http: HTTPClient, routes: Routes) -> None: ...
    async def get_url(self, url: str) -> dict[Any, Any]: ...
