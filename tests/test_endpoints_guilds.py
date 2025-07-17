"""Tests for guilds endpoint."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from ravyapi.api.endpoints.guilds import Guilds
from ravyapi.api.models.guilds import GetGuildResponse


class TestGuilds:
    """Test class for Guilds endpoint."""

    @pytest.fixture
    def mock_http_client(self) -> MagicMock:
        """Create a mock HTTP client."""
        mock = MagicMock()
        mock.get = AsyncMock()
        mock.post = AsyncMock()
        mock.get_permissions = AsyncMock()
        mock.permissions = ["guilds"]
        mock.paths = MagicMock()
        mock.paths.guilds = MagicMock()
        mock.paths.guilds.return_value = MagicMock()
        mock.paths.guilds.return_value.route = "/guilds/123456789"
        return mock

    @pytest.fixture
    def guilds_endpoint(self, mock_http_client: MagicMock) -> Guilds:
        """Create a Guilds endpoint instance."""
        return Guilds(mock_http_client)

    def test_guilds_initialization(self, mock_http_client: MagicMock) -> None:
        """Test Guilds initialization."""
        guilds = Guilds(mock_http_client)
        assert guilds._http is mock_http_client  # type: ignore

    def test_guilds_slots(self, mock_http_client: MagicMock) -> None:
        """Test Guilds has proper slots."""
        guilds = Guilds(mock_http_client)
        assert hasattr(guilds, "__slots__")
        assert guilds.__slots__ == ()

    @pytest.mark.asyncio
    async def test_get_guild_success(
        self, guilds_endpoint: Guilds, mock_http_client: MagicMock
    ) -> None:
        """Test successful get_guild call."""
        guild_id = 123456789
        response_data = {
            "trust": {"level": 3, "label": "Neutral"},
            "bans": [
                {
                    "provider": "ravy",
                    "reason": "Test reason",
                    "moderator": "987654321",
                    "reason_key": "test_key",
                }
            ],
        }

        mock_http_client.get.return_value = response_data

        result = await guilds_endpoint.get_guild(guild_id)

        assert isinstance(result, GetGuildResponse)
        mock_http_client.get.assert_called_once_with(f"/guilds/{guild_id}")

    @pytest.mark.asyncio
    async def test_get_guild_invalid_guild_id_type(
        self, guilds_endpoint: Guilds
    ) -> None:
        """Test get_guild with invalid guild_id type."""
        with pytest.raises(
            TypeError, match='Parameter "guild_id" must be of type "int"'
        ):
            await guilds_endpoint.get_guild("invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_guild_permission_check(
        self, mock_http_client: MagicMock
    ) -> None:
        """Test get_guild permission check."""
        from ravyapi.api.errors import AccessError

        # Create a mock that simulates insufficient permissions
        mock_http_client.permissions = ["other"]
        guilds = Guilds(mock_http_client)

        # Mock the permission check to raise AccessError
        mock_http_client.get_permissions.return_value = ["other"]

        with pytest.raises(AccessError):
            await guilds.get_guild(123456789)
