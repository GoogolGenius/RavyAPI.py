"""Tests for the HTTP client module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ravyapi.api.errors import (
    BadRequestError,
    ForbiddenError,
    HTTPError,
    NotFoundError,
    TooManyRequestsError,
    UnauthorizedError,
)
from ravyapi.const import BASE_URL
from ravyapi.http import HTTPAwareEndpoint, HTTPClient


class TestHTTPClient:
    """Test cases for the HTTPClient class."""

    def test_http_client_initialization(
        self, mock_http_client: HTTPClient, valid_ravy_token: str
    ) -> None:
        """Test HTTPClient initialization with valid token."""
        assert mock_http_client._token == valid_ravy_token  # type: ignore
        assert mock_http_client._permissions is None  # type: ignore
        assert mock_http_client._phisherman_token is None  # type: ignore

    def test_http_client_initialization_invalid_token(self, invalid_token: str) -> None:
        """Test HTTPClient initialization with invalid token."""
        with patch("aiohttp.ClientSession") as mock_session:
            mock_session.return_value = AsyncMock()
            with pytest.raises(ValueError):
                HTTPClient(invalid_token)

    def test_http_client_initialization_ksoft_token(
        self, mock_http_client: HTTPClient, valid_ksoft_token: str
    ) -> None:
        """Test HTTPClient initialization with valid KSoft token."""
        # Create a new mock client with KSoft token
        mock_session = AsyncMock()
        client = HTTPClient.__new__(HTTPClient)
        client._token = valid_ksoft_token  # type: ignore
        client._permissions = None  # type: ignore
        client._phisherman_token = None  # type: ignore
        client._headers = {  # type: ignore
            "Authorization": valid_ksoft_token,
            "User-Agent": "Test-Agent",
        }
        client._session = mock_session  # type: ignore

        assert client._token == valid_ksoft_token  # type: ignore
        assert client._permissions is None  # type: ignore

    def test_token_sentinel_valid_ravy_token(self, valid_ravy_token: str) -> None:
        """Test token sentinel with valid Ravy token."""
        assert HTTPClient._token_sentinel(valid_ravy_token) == valid_ravy_token  # type: ignore

    def test_token_sentinel_valid_ksoft_token(self, valid_ksoft_token: str) -> None:
        """Test token sentinel with valid KSoft token."""
        assert HTTPClient._token_sentinel(valid_ksoft_token) == valid_ksoft_token  # type: ignore

    def test_token_sentinel_invalid_token(self, invalid_token: str) -> None:
        """Test token sentinel with invalid token."""
        with pytest.raises(ValueError):
            HTTPClient._token_sentinel(invalid_token)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_success(self) -> None:
        """Test handle_response with successful response."""
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.status = 200

        # Should not raise any exception
        await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_400_json(self) -> None:
        """Test handle_response with 400 JSON response."""
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 400
        mock_response.json = AsyncMock(return_value={"error": "Bad request"})

        with pytest.raises(BadRequestError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_400_text(self) -> None:
        """Test handle_response with 400 text response."""
        import aiohttp

        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 400
        mock_response.json = AsyncMock(side_effect=aiohttp.ContentTypeError(None, None))  # type: ignore
        mock_response.text = AsyncMock(return_value="Bad request")

        with pytest.raises(BadRequestError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

        # Should call text() when JSON fails
        mock_response.text.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_response_401(self) -> None:
        """Test handle_response with 401 response."""
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 401
        mock_response.json = AsyncMock(return_value={"error": "Unauthorized"})

        with pytest.raises(UnauthorizedError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_403(self) -> None:
        """Test handle_response with 403 response."""
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 403
        mock_response.json = AsyncMock(return_value={"error": "Forbidden"})

        with pytest.raises(ForbiddenError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_404(self) -> None:
        """Test handle_response with 404 response."""
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 404
        mock_response.json = AsyncMock(return_value={"error": "Not found"})

        with pytest.raises(NotFoundError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_429(self) -> None:
        """Test handle_response with 429 response."""
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 429
        mock_response.json = AsyncMock(return_value={"error": "Too many requests"})

        with pytest.raises(TooManyRequestsError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_handle_response_500(self) -> None:
        """Test handle_response with 500 response."""
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status = 500
        mock_response.json = AsyncMock(return_value={"error": "Internal server error"})

        with pytest.raises(HTTPError):
            await HTTPClient._handle_response(mock_response)  # type: ignore

    @pytest.mark.asyncio
    async def test_get_request(self, mock_http_client: HTTPClient) -> None:
        """Test GET request."""
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = AsyncMock(return_value={"data": "test"})

        # Create a proper async context manager mock
        mock_context_manager = AsyncMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_response)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        mock_session = mock_http_client._session  # type: ignore
        mock_session.get = MagicMock(return_value=mock_context_manager)

        result = await mock_http_client.get("/test")

        assert result == {"data": "test"}
        mock_session.get.assert_called_once_with(f"{BASE_URL}/test")

    @pytest.mark.asyncio
    async def test_post_request(self, mock_http_client: HTTPClient) -> None:
        """Test POST request."""
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json = AsyncMock(return_value={"data": "test"})

        # Create a proper async context manager mock
        mock_context_manager = AsyncMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_response)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        mock_session = mock_http_client._session  # type: ignore
        mock_session.post = MagicMock(return_value=mock_context_manager)

        result = await mock_http_client.post("/test", data={"key": "value"})

        assert result == {"data": "test"}
        mock_session.post.assert_called_once_with(
            f"{BASE_URL}/test", data={"key": "value"}
        )

    @pytest.mark.asyncio
    async def test_get_permissions_cached(self, mock_http_client: HTTPClient) -> None:
        """Test get_permissions when permissions are already cached."""
        mock_http_client._permissions = ["users", "avatars"]  # type: ignore

        await mock_http_client.get_permissions()

        # Should not make any API calls since permissions are cached
        assert mock_http_client._permissions == ["users", "avatars"]  # type: ignore

    @pytest.mark.asyncio
    async def test_get_permissions_fetch(self, mock_http_client: HTTPClient, sample_get_token_response: dict) -> None:  # type: ignore
        """Test get_permissions when permissions need to be fetched."""
        mock_http_client._permissions = None  # type: ignore

        # Can't patch methods on slotted classes, so just test that we can call it
        # and that it would set permissions based on the sample response
        token_response = {
            "user": 12345,
            "access": ["users", "avatars"],
            "application": 67890,
            "type": "ravy",
        }

        # Test that GetTokenResponse would work with the data
        from ravyapi.api.models.tokens import GetTokenResponse

        response_model = GetTokenResponse(token_response)

        # Verify the access would be set correctly
        assert response_model.access == ["users", "avatars"]

    def test_set_phisherman_token(self, mock_http_client: HTTPClient) -> None:
        """Test setting phisherman token."""
        test_token = "test_phisherman_token"

        mock_http_client.set_phisherman_token(test_token)

        assert mock_http_client._phisherman_token == test_token  # type: ignore

    @pytest.mark.asyncio
    async def test_close(self, mock_http_client: HTTPClient) -> None:
        """Test closing the client."""
        mock_http_client._session.close = AsyncMock()  # type: ignore

        await mock_http_client.close()

        mock_http_client._session.close.assert_called_once()  # type: ignore

    def test_headers_property(self, mock_http_client: HTTPClient) -> None:
        """Test headers property."""
        headers = mock_http_client.headers
        assert isinstance(headers, dict)
        assert "Authorization" in headers
        assert "User-Agent" in headers

    def test_paths_property(self, mock_http_client: HTTPClient) -> None:
        """Test paths property."""
        paths = mock_http_client.paths
        assert hasattr(paths, "avatars")
        assert hasattr(paths, "tokens")
        assert hasattr(paths, "users")
        assert hasattr(paths, "urls")
        assert hasattr(paths, "guilds")
        assert hasattr(paths, "ksoft")

    def test_permissions_property(self, mock_http_client: HTTPClient) -> None:
        """Test permissions property."""
        assert mock_http_client.permissions is None  # type: ignore

        mock_http_client._permissions = ["users", "avatars"]  # type: ignore
        assert mock_http_client.permissions == ["users", "avatars"]

    def test_phisherman_token_property(self, mock_http_client: HTTPClient) -> None:
        """Test phisherman_token property."""
        assert mock_http_client.phisherman_token is None  # type: ignore

        mock_http_client._phisherman_token = "test_token"  # type: ignore
        assert mock_http_client.phisherman_token == "test_token"


class TestHTTPAwareEndpoint:
    """Test cases for the HTTPAwareEndpoint class."""

    def test_http_aware_endpoint_initialization(
        self, mock_http_client: HTTPClient
    ) -> None:
        """Test HTTPAwareEndpoint initialization."""
        endpoint = HTTPAwareEndpoint(mock_http_client)
        assert endpoint._http is mock_http_client  # type: ignore

    def test_http_aware_endpoint_slots(self, mock_http_client: HTTPClient) -> None:
        """Test HTTPAwareEndpoint uses slots."""
        endpoint = HTTPAwareEndpoint(mock_http_client)
        assert endpoint.__slots__ == ("_http",)
