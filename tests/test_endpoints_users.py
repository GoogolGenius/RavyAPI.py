"""Tests for users endpoint."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock

import pytest

from ravyapi.api.endpoints.users import Users
from ravyapi.api.models.users import (
    GetBansResponse,
    GetPronounsResponse,
    GetReputationResponse,
    GetUserResponse,
    GetWhitelistsResponse,
)


class TestUsers:
    """Test class for Users endpoint."""

    @pytest.fixture
    def mock_http_client(self):
        """Create a mock HTTP client."""
        from unittest.mock import MagicMock

        mock = AsyncMock()
        mock.get_permissions = AsyncMock()
        mock.permissions = [
            "users",
            "admin.users",
            "users.pronouns",
            "admin.bans",
            "users.bans",
        ]
        mock.paths = MagicMock()
        mock.paths.users = MagicMock()
        mock.paths.users.return_value = MagicMock()
        mock.paths.users.return_value.route = "/users/123456789"
        mock.post = AsyncMock()
        mock.delete = AsyncMock()
        return mock

    def test_users_initialization(self, mock_http_client: AsyncMock) -> None:
        """Test Users initialization."""
        users = Users(mock_http_client)
        assert users._http is mock_http_client  # type: ignore

    def test_users_slots(self, mock_http_client: AsyncMock) -> None:
        """Test Users has proper slots."""
        users = Users(mock_http_client)
        assert hasattr(users, "__slots__")
        assert users.__slots__ == ()

    @pytest.mark.asyncio
    async def test_get_user_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful get_user call."""
        user_id = 123456789
        response_data: dict[str, Any] = {
            "trust": {"level": 3, "label": "Neutral"},
            "bans": [],
            "whitelists": [],
            "pronouns": "he/him",
            "rep": [],
            "sentinel": {
                "isSentinel": False,
                "permissions": [],
                "verified": False,
                "id": "123",
            },
        }

        users = Users(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await users.get_user(user_id)

        assert isinstance(result, GetUserResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.users(user_id).route
        )

    @pytest.mark.asyncio
    async def test_get_user_invalid_user_id_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_user with invalid user_id type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await users.get_user("invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_pronouns_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful get_pronouns call."""
        user_id = 123456789
        response_data = {"pronouns": "they/them"}

        users = Users(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await users.get_pronouns(user_id)

        assert isinstance(result, GetPronounsResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.users(user_id).pronouns
        )

    @pytest.mark.asyncio
    async def test_get_pronouns_invalid_user_id_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_pronouns with invalid user_id type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await users.get_pronouns("invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_bans_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful get_bans call."""
        user_id = 123456789
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

        users = Users(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await users.get_bans(user_id)

        assert isinstance(result, GetBansResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.users(user_id).bans
        )

    @pytest.mark.asyncio
    async def test_get_bans_invalid_user_id_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_bans with invalid user_id type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await users.get_bans("invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_add_ban_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful add_ban call."""
        user_id = 123456789
        provider = "ravy"
        reason = "Test ban reason"
        moderator = 987654321
        reason_key = "test_key"

        users = Users(mock_http_client)
        mock_http_client.post.return_value = None

        await users.add_ban(
            user_id,
            provider=provider,
            reason=reason,
            moderator=moderator,
            reason_key=reason_key,
        )

        expected_json = {
            "provider": provider,
            "reason": reason,
            "moderator": str(moderator),
            "reason_key": reason_key,
        }
        mock_http_client.post.assert_called_once_with(
            mock_http_client.paths.users(user_id).bans, json=expected_json
        )

    @pytest.mark.asyncio
    async def test_add_ban_without_reason_key(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test add_ban without reason_key."""
        user_id = 123456789
        provider = "ravy"
        reason = "Test ban reason"
        moderator = 987654321

        users = Users(mock_http_client)
        mock_http_client.post.return_value = None

        await users.add_ban(
            user_id, provider=provider, reason=reason, moderator=moderator
        )

        expected_json = {
            "provider": provider,
            "reason": reason,
            "moderator": str(moderator),
        }
        mock_http_client.post.assert_called_once_with(
            mock_http_client.paths.users(user_id).bans, json=expected_json
        )

    @pytest.mark.asyncio
    async def test_add_ban_invalid_user_id_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test add_ban with invalid user_id type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await users.add_ban(
                "invalid", provider="ravy", reason="test", moderator=123  # type: ignore
            )

    @pytest.mark.asyncio
    async def test_add_ban_invalid_provider_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test add_ban with invalid provider type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "provider" must be of type "str"'
        ):
            await users.add_ban(123, provider=123, reason="test", moderator=123)  # type: ignore

    @pytest.mark.asyncio
    async def test_add_ban_empty_provider(self, mock_http_client: AsyncMock) -> None:
        """Test add_ban with empty provider."""
        users = Users(mock_http_client)

        with pytest.raises(ValueError, match='Parameter "provider" must not be empty'):
            await users.add_ban(123, provider="", reason="test", moderator=123)

    @pytest.mark.asyncio
    async def test_add_ban_invalid_reason_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test add_ban with invalid reason type."""
        users = Users(mock_http_client)

        with pytest.raises(TypeError, match='Parameter "reason" must be of type "str"'):
            await users.add_ban(123, provider="ravy", reason=123, moderator=123)  # type: ignore

    @pytest.mark.asyncio
    async def test_add_ban_empty_reason(self, mock_http_client: AsyncMock) -> None:
        """Test add_ban with empty reason."""
        users = Users(mock_http_client)

        with pytest.raises(ValueError, match='Parameter "reason" must not be empty'):
            await users.add_ban(123, provider="ravy", reason="", moderator=123)

    @pytest.mark.asyncio
    async def test_add_ban_invalid_moderator_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test add_ban with invalid moderator type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "moderator" must be of type "int"'
        ):
            await users.add_ban(
                123, provider="ravy", reason="test", moderator="invalid"  # type: ignore
            )

    @pytest.mark.asyncio
    async def test_add_ban_invalid_reason_key_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test add_ban with invalid reason_key type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "reason_key" must be of type "str"'
        ):
            await users.add_ban(
                123, provider="ravy", reason="test", moderator=123, reason_key=123  # type: ignore
            )

    @pytest.mark.asyncio
    async def test_add_ban_empty_reason_key(self, mock_http_client: AsyncMock) -> None:
        """Test add_ban with empty reason_key."""
        users = Users(mock_http_client)

        with pytest.raises(
            ValueError, match='Parameter "reason_key" must not be empty'
        ):
            await users.add_ban(
                123, provider="ravy", reason="test", moderator=123, reason_key=""
            )

    @pytest.mark.asyncio
    async def test_get_whitelists_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful get_whitelists call."""
        user_id = 123456789
        response_data = {
            "trust": {"level": 5, "label": "Trusted"},
            "whitelists": [
                {"provider": "ravy", "reason": "Staff member"},
                {"provider": "dservices", "reason": "Trusted user"},
            ],
        }

        users = Users(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await users.get_whitelists(user_id)

        assert isinstance(result, GetWhitelistsResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.users(user_id).whitelists
        )

    @pytest.mark.asyncio
    async def test_get_whitelists_invalid_user_id_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_whitelists with invalid user_id type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await users.get_whitelists("invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_reputation_success(self, mock_http_client: AsyncMock) -> None:
        """Test successful get_reputation call."""
        user_id = 123456789
        response_data = {
            "trust": {"level": 4, "label": "Trusted"},
            "rep": [{"provider": "ravy", "score": 0.8, "upvotes": 10, "downvotes": 2}],
        }

        users = Users(mock_http_client)
        mock_http_client.get.return_value = response_data

        result = await users.get_reputation(user_id)

        assert isinstance(result, GetReputationResponse)
        mock_http_client.get.assert_called_once_with(
            mock_http_client.paths.users(user_id).reputation
        )

    @pytest.mark.asyncio
    async def test_get_reputation_invalid_user_id_type(
        self, mock_http_client: AsyncMock
    ) -> None:
        """Test get_reputation with invalid user_id type."""
        users = Users(mock_http_client)

        with pytest.raises(
            TypeError, match='Parameter "user_id" must be of type "int"'
        ):
            await users.get_reputation("invalid")  # type: ignore
