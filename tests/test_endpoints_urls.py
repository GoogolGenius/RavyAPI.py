"""Tests for URLs endpoint."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest
from aioresponses import aioresponses

from ravyapi.api.endpoints.urls import URLs
from ravyapi.api.models.urls import GetWebsiteResponse


class TestURLs:
    """Test class for URLs endpoint."""

    @pytest.fixture
    def mock_http_client(self) -> AsyncMock:
        """Create a mock HTTP client."""
        mock = AsyncMock()
        mock.get_permissions = AsyncMock()
        mock.permissions = ["urls.cached", "admin.urls"]
        mock.phisherman_token = None
        mock.paths = AsyncMock()
        mock.paths.urls = AsyncMock()
        mock.paths.urls.route = "/urls"
        mock.post = AsyncMock()
        return mock

    def test_urls_initialization(self, mock_http_client: AsyncMock) -> None:
        """Test URLs initialization."""
        urls = URLs(mock_http_client)
        assert urls._http is mock_http_client  # type: ignore

    def test_urls_slots(self, mock_http_client: AsyncMock) -> None:
        """Test URLs has proper slots."""
        urls = URLs(mock_http_client)
        assert hasattr(urls, "__slots__")
        assert urls.__slots__ == ()

    @pytest.mark.asyncio
    async def test_get_website_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful get_website call."""
        url = "https://example.com"
        response_data = {
            "isFraudulent": False,
            "message": "Safe website",
            "scan_date": "2023-01-01T00:00:00Z",
        }

        urls = URLs(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await urls.get_website(url)

        assert isinstance(result, GetWebsiteResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.urls.route, params={"url": url}
        )

    @pytest.mark.asyncio
    async def test_get_website_with_author(self, mock_http_client: AsyncMock) -> None:
        """Test get_website with author parameter."""
        url = "https://example.com"
        author = 123456789
        response_data = {
            "isFraudulent": False,
            "message": "Safe website",
            "scan_date": "2023-01-01T00:00:00Z",
        }

        urls = URLs(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await urls.get_website(url, author=author)

        assert isinstance(result, GetWebsiteResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.urls.route, params={"url": url, "author": author}
        )

    @pytest.mark.asyncio
    async def test_get_website_with_phisherman(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_website with phisherman parameters."""
        url = "https://example.com"
        phisherman_user = 123456789
        phisherman_token = "test_token"
        response_data = {
            "isFraudulent": False,
            "message": "Safe website",
            "scan_date": "2023-01-01T00:00:00Z",
        }

        urls = URLs(mock_http_client)
        mock_http_client.phisherman_token = phisherman_token
        mock_http_client.get.return_value = response_data

        result = await urls.get_website(url, phisherman_user=phisherman_user)

        assert isinstance(result, GetWebsiteResponse)
        expected_params = {
            "url": url,
            "phisherman_token": phisherman_token,
            "phisherman_user": phisherman_user,
        }
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.urls.route, params=expected_params
        )

    @pytest.mark.asyncio
    async def test_get_website_invalid_url_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_website with invalid url type."""
        urls = URLs(mock_http_client)

        with pytest.raises(TypeError, match='Parameter "url" must be of type "str"'):
            await urls.get_website(123)  # type: ignore

    @pytest.mark.asyncio
    async def test_get_website_empty_url(self, mock_http_client: AsyncMock) -> None:
        """Test get_website with empty url."""
        urls = URLs(mock_http_client)

        with pytest.raises(ValueError, match='Parameter "url" must not empty'):
            await urls.get_website("")

    @pytest.mark.asyncio
    async def test_get_website_invalid_author_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_website with invalid author type."""
        urls = URLs(mock_http_client)

        with pytest.raises(TypeError, match='Parameter "author" must be of type "int"'):
            await urls.get_website("https://example.com", author="invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_website_invalid_phisherman_user_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_website with invalid phisherman_user type."""
        urls = URLs(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "phisherman_user" must be of type "int"'
        ):
            await urls.get_website("https://example.com", phisherman_user="invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_website_phisherman_token_required(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_website phisherman token required when user is set."""
        urls = URLs(mock_http_client)
        mock_http_client.phisherman_token = None

        with pytest.raises(
            ValueError, match="Phisherman token required if phisherman user is set."
        ):
            await urls.get_website("https://example.com", phisherman_user=123)

    @pytest.mark.asyncio
    async def test_get_website_phisherman_user_required(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_website phisherman user required when token is set."""
        urls = URLs(mock_http_client)
        mock_http_client.phisherman_token = "test_token"

        with pytest.raises(
            ValueError, match="Phisherman user required if phisherman token is set."
        ):
            await urls.get_website("https://example.com")

    @pytest.mark.asyncio
    async def test_edit_website_success(
        self, mock_http_client: AsyncMock, mock_aioresponses: aioresponses
    ) -> None:
        """Test successful edit_website call."""
        url = "https://example.com"
        is_fraudulent = True
        message = "Fraudulent website"

        mock_aioresponses.post(f"https://ravy.org/api/v1/urls/{url}", payload={})  # type: ignore

        urls = URLs(mock_http_client)
        mock_http_client.post.return_value = None

        await urls.edit_website(url, is_fraudulent=is_fraudulent, message=message)

        expected_json = {"isFraudulent": is_fraudulent, "message": "Fraudulent+website"}
        mock_http_client.post.assert_called_once_with(
            f"/urls/{url}", json=expected_json
        )

    @pytest.mark.asyncio
    async def test_edit_website_with_encoding(
        self, mock_http_client: AsyncMock, mock_aioresponses: aioresponses
    ) -> None:
        """Test edit_website with URL encoding."""
        url = "https://example.com"
        is_fraudulent = True
        message = "Fraudulent website with spaces"

        urls = URLs(mock_http_client)
        mock_http_client.post.return_value = None

        await urls.edit_website(
            url, is_fraudulent=is_fraudulent, message=message, encode=True
        )

        expected_json = {
            "isFraudulent": is_fraudulent,
            "message": "Fraudulent+website+with+spaces",
        }
        mock_http_client.post.assert_called_once_with(
            f"/urls/{url}", json=expected_json
        )

    @pytest.mark.asyncio
    async def test_edit_website_invalid_url_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test edit_website with invalid url type."""
        urls = URLs(mock_http_client)

        with pytest.raises(TypeError, match='Parameter "url" must be of type "str"'):
            await urls.edit_website(123, is_fraudulent=True, message="test")  # type: ignore

    @pytest.mark.asyncio
    async def test_edit_website_empty_url(self, mock_http_client: AsyncMock) -> None:
        """Test edit_website with empty url."""
        urls = URLs(mock_http_client)

        with pytest.raises(ValueError, match='Parameter "url" must not be empty'):
            await urls.edit_website("", is_fraudulent=True, message="test")

    @pytest.mark.asyncio
    async def test_edit_website_invalid_is_fraudulent_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test edit_website with invalid is_fraudulent type."""
        urls = URLs(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "is_fraudulent" must be of type "bool"'
        ):
            await urls.edit_website(
                "https://example.com", is_fraudulent="invalid", message="test"  # type: ignore
            )

    @pytest.mark.asyncio
    async def test_edit_website_invalid_message_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test edit_website with invalid message type."""
        urls = URLs(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "message" must be of type "str"'
        ):
            await urls.edit_website(
                "https://example.com", is_fraudulent=True, message=123  # type: ignore
            )

    @pytest.mark.asyncio
    async def test_edit_website_empty_message(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test edit_website with empty message."""
        urls = URLs(mock_http_client)

        with pytest.raises(ValueError, match='Parameter "message" must not be empty'):
            await urls.edit_website(
                "https://example.com", is_fraudulent=True, message=""
            )

    @pytest.mark.asyncio
    async def test_edit_website_invalid_encode_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test edit_website with invalid encode type."""
        urls = URLs(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "encode" must be of type "bool"'
        ):
            await urls.edit_website(
                "https://example.com",
                is_fraudulent=True,
                message="test",
                encode="invalid",  # type: ignore
            )

    @pytest.mark.asyncio
    async def test_edit_website_permission_check(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test edit_website permission check."""
        urls = URLs(mock_http_client)
        mock_http_client.permissions = ["other"]

        with pytest.raises(Exception):  # Should raise AccessError or similar
            await urls.edit_website(
                "https://example.com", is_fraudulent=True, message="test"
            )
