"""Tests for KSoft endpoint."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from ravyapi.api.endpoints.ksoft import KSoft
from ravyapi.api.models.ksoft import GetKSoftBanResponse


class TestKSoft:
    """Test class for KSoft endpoint."""

    @pytest.fixture
    def mock_http_client(self) -> MagicMock:
        """Create a mock HTTP client."""
        mock = MagicMock()
        mock.get = AsyncMock()
        mock.post = AsyncMock()
        mock.get_permissions = AsyncMock()
        mock.permissions = ["ksoft.bans"]
        mock.paths = MagicMock()
        mock.paths.ksoft = MagicMock()
        mock.paths.ksoft.bans = MagicMock()
        mock.paths.ksoft.bans.return_value = "/ksoft/bans/123456789"
        return mock

    @pytest.fixture
    def ksoft_endpoint(self, mock_http_client: MagicMock) -> KSoft:
        """Create a KSoft endpoint instance."""
        return KSoft(mock_http_client)

    def test_ksoft_initialization(self, mock_http_client: MagicMock) -> None:
        """Test KSoft initialization."""
        ksoft = KSoft(mock_http_client)
        assert ksoft._http is mock_http_client  # type: ignore

    def test_ksoft_slots(self, mock_http_client: MagicMock) -> None:
        """Test KSoft has proper slots."""
        ksoft = KSoft(mock_http_client)
        assert hasattr(ksoft, "__slots__")
        assert ksoft.__slots__ == ()

    @pytest.mark.asyncio
    async def test_get_ban_success(
        self, ksoft_endpoint: KSoft, mock_http_client: MagicMock
    ) -> None:
        """Test successful get_ban call."""
        user_id = 123456789
        response_data = {
            "found": True,
            "id": "123456789",
            "tag": "TestUser#1234",
            "reason": "Test ban reason",
            "proof": "https://example.com/proof",
            "moderator": "987654321",
            "severe": True,
            "timestamp": "2023-01-01T00:00:00Z",
        }

        mock_http_client.get.return_value = response_data

        result = await ksoft_endpoint.get_ban(user_id)

        assert isinstance(result, GetKSoftBanResponse)
        mock_http_client.get.assert_called_once_with(f"/ksoft/bans/{user_id}")

    @pytest.mark.asyncio
    async def test_get_ban_invalid_user_id_type(self, ksoft_endpoint: KSoft) -> None:
        """Test get_ban with invalid user_id type."""
        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await ksoft_endpoint.get_ban("invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_ban_permission_check(self, mock_http_client: MagicMock) -> None:
        """Test get_ban permission check."""
        from ravyapi.api.errors import AccessError

        # Create a mock that simulates insufficient permissions
        mock_http_client.permissions = ["other"]
        ksoft = KSoft(mock_http_client)

        # Mock the permission check to raise AccessError
        mock_http_client.get_permissions.return_value = ["other"]

        with pytest.raises(AccessError):
            await ksoft.get_ban(123456789)
