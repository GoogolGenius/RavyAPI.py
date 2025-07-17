"""Tests for guilds models."""

from __future__ import annotations

from typing import Any

from ravyapi.api.models.generic.ban_entry import BanEntryResponse
from ravyapi.api.models.generic.trust import Trust
from ravyapi.api.models.guilds import GetGuildResponse


class TestGetGuildResponse:
    """Test class for GetGuildResponse model."""

    def test_get_guild_response_initialization(self):
        """Test GetGuildResponse initialization."""
        data: dict[str, Any] = {
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

        response = GetGuildResponse(data)

        assert response.data == data
        assert isinstance(response.trust, Trust)
        assert response.trust.level == 3
        assert response.trust.label == "Neutral"
        assert isinstance(response.bans, list)
        assert len(response.bans) == 1
        assert isinstance(response.bans[0], BanEntryResponse)
        assert response.bans[0].provider == "ravy"
        assert response.bans[0].reason == "Test reason"

    def test_get_guild_response_empty_bans(self):
        """Test GetGuildResponse with empty bans list."""
        data: dict[str, Any] = {"trust": {"level": 5, "label": "Trusted"}, "bans": []}

        response = GetGuildResponse(data)

        assert response.data == data
        assert isinstance(response.trust, Trust)
        assert response.trust.level == 5
        assert response.trust.label == "Trusted"
        assert isinstance(response.bans, list)
        assert len(response.bans) == 0

    def test_get_guild_response_multiple_bans(self):
        """Test GetGuildResponse with multiple bans."""
        data = {
            "trust": {"level": 1, "label": "Untrusted"},
            "bans": [
                {
                    "provider": "ravy",
                    "reason": "First ban",
                    "moderator": "111111111",
                    "reason_key": "first_key",
                },
                {
                    "provider": "dservices",
                    "reason": "Second ban",
                    "moderator": "222222222",
                },
            ],
        }

        response = GetGuildResponse(data)

        assert response.data == data
        assert isinstance(response.trust, Trust)
        assert response.trust.level == 1
        assert response.trust.label == "Untrusted"
        assert isinstance(response.bans, list)
        assert len(response.bans) == 2

        # Check first ban
        assert isinstance(response.bans[0], BanEntryResponse)
        assert response.bans[0].provider == "ravy"
        assert response.bans[0].reason == "First ban"
        assert response.bans[0].moderator == 111111111
        assert response.bans[0].reason_key == "first_key"

        # Check second ban
        assert isinstance(response.bans[1], BanEntryResponse)
        assert response.bans[1].provider == "dservices"
        assert response.bans[1].reason == "Second ban"
        assert response.bans[1].moderator == 222222222
        assert response.bans[1].reason_key is None

    def test_get_guild_response_repr(self):
        """Test GetGuildResponse repr."""
        data = {
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

        response = GetGuildResponse(data)
        repr_str = repr(response)

        assert "GetGuildResponse" in repr_str
        assert "trust=" in repr_str
        assert "bans=" in repr_str

    def test_get_guild_response_data_property(self):
        """Test GetGuildResponse data property."""
        data: dict[str, Any] = {
            "trust": {"level": 3, "label": "Neutral"},
            "bans": [],
        }

        response = GetGuildResponse(data)

        assert response.data is data
        assert isinstance(response.data, dict)

    def test_get_guild_response_trust_property(self):
        """Test GetGuildResponse trust property."""
        data: dict[str, Any] = {
            "trust": {"level": 4, "label": "Somewhat Trusted"},
            "bans": [],
        }

        response = GetGuildResponse(data)

        assert isinstance(response.trust, Trust)
        assert response.trust.level == 4
        assert response.trust.label == "Somewhat Trusted"

    def test_get_guild_response_bans_property(self):
        """Test GetGuildResponse bans property."""
        data = {
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

        response = GetGuildResponse(data)

        assert isinstance(response.bans, list)
        assert len(response.bans) == 1
        assert isinstance(response.bans[0], BanEntryResponse)

    def test_get_guild_response_slots(self):
        """Test GetGuildResponse has proper slots."""
        data: dict[str, Any] = {
            "trust": {"level": 3, "label": "Neutral"},
            "bans": [],
        }

        response = GetGuildResponse(data)

        assert hasattr(response, "__slots__")
        expected_slots = ("_data", "_trust", "_bans")
        assert response.__slots__ == expected_slots

    def test_get_guild_response_immutable_data(self):
        """Test GetGuildResponse data is immutable reference."""
        data: dict[str, Any] = {"trust": {"level": 3, "label": "Neutral"}, "bans": []}

        response = GetGuildResponse(data)
        original_data = response.data

        # Modify original data
        data["trust"]["level"] = 5

        # Response data should reflect the change since it's a reference
        assert response.data["trust"]["level"] == 5
        assert response.data is original_data

    def test_get_guild_response_complex_data(self):
        """Test GetGuildResponse with complex data structure."""
        data = {
            "trust": {"level": 6, "label": "Highly Trusted"},
            "bans": [
                {
                    "provider": "ravy",
                    "reason": "Complex ban reason with special chars: åäö",
                    "moderator": "999999999",
                    "reason_key": "complex_key_123",
                }
            ],
        }

        response = GetGuildResponse(data)

        assert response.data == data
        assert response.trust.level == 6
        assert response.trust.label == "Highly Trusted"
        assert len(response.bans) == 1
        assert response.bans[0].reason == "Complex ban reason with special chars: åäö"
        assert response.bans[0].moderator == 999999999
        assert response.bans[0].reason_key == "complex_key_123"
