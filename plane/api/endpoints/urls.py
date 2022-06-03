from __future__ import annotations

__all__: tuple[str, ...] = ("URLs",)

from plane.api.models import GetWebsiteResponse
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
            raise ValueError('Parameter "phisherman_user" must be of "int" or derivative type')
        
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
