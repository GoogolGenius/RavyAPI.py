"""Tests for generic models."""

from __future__ import annotations

from ravyapi.api.models.generic.ban_entry import BanEntryRequest, BanEntryResponse
from ravyapi.api.models.generic.trust import Trust


class TestBanEntryResponse:
    """Test class for BanEntryResponse model."""

    def test_ban_entry_response_initialization(self):
        """Test BanEntryResponse initialization."""
        data = {
            "provider": "ravy",
            "reason": "Test reason",
            "moderator": "123456789",
            "reason_key": "test_key",
        }

        response = BanEntryResponse(data)

        assert response.data == data
        assert response.provider == "ravy"
        assert response.reason == "Test reason"
        assert response.moderator == 123456789
        assert response.reason_key == "test_key"

    def test_ban_entry_response_without_reason_key(self):
        """Test BanEntryResponse without reason_key."""
        data = {"provider": "ravy", "reason": "Test reason", "moderator": "123456789"}

        response = BanEntryResponse(data)

        assert response.data == data
        assert response.provider == "ravy"
        assert response.reason == "Test reason"
        assert response.moderator == 123456789
        assert response.reason_key is None

    def test_ban_entry_response_repr(self):
        """Test BanEntryResponse repr."""
        data = {
            "provider": "ravy",
            "reason": "Test reason",
            "moderator": "123456789",
            "reason_key": "test_key",
        }

        response = BanEntryResponse(data)
        repr_str = repr(response)

        assert "BanEntryResponse" in repr_str
        assert "provider='ravy'" in repr_str
        assert "reason='Test reason'" in repr_str
        assert "moderator=123456789" in repr_str
        assert "reason_key='test_key'" in repr_str

    def test_ban_entry_response_repr_none_reason_key(self):
        """Test BanEntryResponse repr with None reason_key."""
        data = {"provider": "ravy", "reason": "Test reason", "moderator": "123456789"}

        response = BanEntryResponse(data)
        repr_str = repr(response)

        assert "BanEntryResponse" in repr_str
        assert "provider='ravy'" in repr_str
        assert "reason='Test reason'" in repr_str
        assert "moderator=123456789" in repr_str
        assert "reason_key=None" in repr_str

    def test_ban_entry_response_data_property(self):
        """Test BanEntryResponse data property."""
        data = {
            "provider": "ravy",
            "reason": "Test reason",
            "moderator": "123456789",
            "reason_key": "test_key",
        }

        response = BanEntryResponse(data)

        assert response.data is data
        assert isinstance(response.data, dict)

    def test_ban_entry_response_string_moderator(self):
        """Test BanEntryResponse with string moderator conversion."""
        data = {
            "provider": "ravy",
            "reason": "Test reason",
            "moderator": "123456789",
            "reason_key": "test_key",
        }

        response = BanEntryResponse(data)

        assert response.moderator == 123456789
        assert isinstance(response.moderator, int)

    def test_ban_entry_response_slots(self):
        """Test BanEntryResponse has proper slots."""
        data = {
            "provider": "ravy",
            "reason": "Test reason",
            "moderator": "123456789",
            "reason_key": "test_key",
        }

        response = BanEntryResponse(data)

        assert hasattr(response, "__slots__")
        expected_slots = ("_data", "_provider", "_reason", "_reason_key", "_moderator")
        assert response.__slots__ == expected_slots

    def test_ban_entry_response_immutable_data(self):
        """Test BanEntryResponse data is immutable reference."""
        data = {
            "provider": "ravy",
            "reason": "Test reason",
            "moderator": "123456789",
            "reason_key": "test_key",
        }

        response = BanEntryResponse(data)
        original_data = response.data

        # Modify original data
        data["provider"] = "modified"

        # Response data should reflect the change since it's a reference
        assert response.data["provider"] == "modified"
        assert response.data is original_data


class TestBanEntryRequest:
    """Test class for BanEntryRequest model."""

    def test_ban_entry_request_initialization(self):
        """Test BanEntryRequest initialization."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789
        reason_key = "test_key"

        request = BanEntryRequest(provider, reason, moderator, reason_key)

        assert request.provider == provider
        assert request.reason == reason
        assert request.moderator == moderator
        assert request.reason_key == reason_key

    def test_ban_entry_request_without_reason_key(self):
        """Test BanEntryRequest without reason_key."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789

        request = BanEntryRequest(provider, reason, moderator)

        assert request.provider == provider
        assert request.reason == reason
        assert request.moderator == moderator
        assert request.reason_key is None

    def test_ban_entry_request_repr(self):
        """Test BanEntryRequest repr."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789
        reason_key = "test_key"

        request = BanEntryRequest(provider, reason, moderator, reason_key)
        repr_str = repr(request)

        assert "BanEntryRequest" in repr_str
        assert "provider='ravy'" in repr_str
        assert "reason='Test reason'" in repr_str
        assert "moderator=123456789" in repr_str
        assert "reason_key='test_key'" in repr_str

    def test_ban_entry_request_repr_none_reason_key(self):
        """Test BanEntryRequest repr with None reason_key."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789

        request = BanEntryRequest(provider, reason, moderator)
        repr_str = repr(request)

        assert "BanEntryRequest" in repr_str
        assert "provider='ravy'" in repr_str
        assert "reason='Test reason'" in repr_str
        assert "moderator=123456789" in repr_str
        assert "reason_key=None" in repr_str

    def test_ban_entry_request_to_json(self):
        """Test BanEntryRequest to_json method."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789
        reason_key = "test_key"

        request = BanEntryRequest(provider, reason, moderator, reason_key)
        json_data = request.to_json()

        expected = {
            "provider": provider,
            "reason": reason,
            "moderator": str(moderator),
            "reason_key": reason_key,
        }

        assert json_data == expected

    def test_ban_entry_request_to_json_without_reason_key(self):
        """Test BanEntryRequest to_json method without reason_key."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789

        request = BanEntryRequest(provider, reason, moderator)
        json_data = request.to_json()

        expected = {"provider": provider, "reason": reason, "moderator": str(moderator)}

        assert json_data == expected
        assert "reason_key" not in json_data

    def test_ban_entry_request_slots(self):
        """Test BanEntryRequest has proper slots."""
        provider = "ravy"
        reason = "Test reason"
        moderator = 123456789
        reason_key = "test_key"

        request = BanEntryRequest(provider, reason, moderator, reason_key)

        assert hasattr(request, "__slots__")
        expected_slots = ("_provider", "_reason", "_moderator", "_reason_key")
        assert request.__slots__ == expected_slots


class TestTrust:
    """Test class for Trust model."""

    def test_trust_initialization(self):
        """Test Trust initialization."""
        data = {"level": 3, "label": "Neutral"}

        trust = Trust(data)

        assert trust.data == data
        assert trust.level == 3
        assert trust.label == "Neutral"

    def test_trust_repr(self):
        """Test Trust repr."""
        data = {"level": 3, "label": "Neutral"}

        trust = Trust(data)
        repr_str = repr(trust)

        assert "Trust" in repr_str
        assert "level=3" in repr_str
        assert "label='Neutral'" in repr_str

    def test_trust_data_property(self):
        """Test Trust data property."""
        data = {"level": 3, "label": "Neutral"}

        trust = Trust(data)

        assert trust.data is data
        assert isinstance(trust.data, dict)

    def test_trust_level_property(self):
        """Test Trust level property."""
        data = {"level": 5, "label": "Trusted"}

        trust = Trust(data)

        assert trust.level == 5
        assert isinstance(trust.level, int)

    def test_trust_label_property(self):
        """Test Trust label property."""
        data = {"level": 1, "label": "Untrusted"}

        trust = Trust(data)

        assert trust.label == "Untrusted"
        assert isinstance(trust.label, str)

    def test_trust_boundary_levels(self):
        """Test Trust with boundary level values."""
        # Test minimum level
        data_min = {"level": 0, "label": "Minimum"}
        trust_min = Trust(data_min)
        assert trust_min.level == 0
        assert trust_min.label == "Minimum"

        # Test maximum level
        data_max = {"level": 6, "label": "Maximum"}
        trust_max = Trust(data_max)
        assert trust_max.level == 6
        assert trust_max.label == "Maximum"

    def test_trust_slots(self):
        """Test Trust has proper slots."""
        data = {"level": 3, "label": "Neutral"}

        trust = Trust(data)

        assert hasattr(trust, "__slots__")
        expected_slots = ("_data", "_level", "_label")
        assert trust.__slots__ == expected_slots

    def test_trust_immutable_data(self):
        """Test Trust data is immutable reference."""
        data = {"level": 3, "label": "Neutral"}

        trust = Trust(data)
        original_data = trust.data

        # Modify original data
        data["level"] = 5

        # Trust data should reflect the change since it's a reference
        assert trust.data["level"] == 5
        assert trust.data is original_data
