"""Tests for KSoft models."""

from __future__ import annotations

from ravyapi.api.models.ksoft import GetKSoftBanResponse


class TestGetKSoftBanResponse:
    """Test class for GetKSoftBanResponse model."""

    def test_get_ksoft_ban_response_found_true(self):
        """Test GetKSoftBanResponse with found=True."""
        data = {
            "found": True,
            "id": "123456789",
            "tag": "TestUser#1234",
            "reason": "Test ban reason",
            "proof": "https://example.com/proof",
            "moderator": "987654321",
            "severe": True,
            "timestamp": "2023-01-01T00:00:00Z",
        }

        response = GetKSoftBanResponse(data)

        assert response.data == data
        assert response.found is True
        assert response.user_id == 123456789
        assert response.tag == "TestUser#1234"
        assert response.reason == "Test ban reason"
        assert response.proof == "https://example.com/proof"
        assert response.moderator == 987654321
        assert response.severe is True
        assert response.timestamp == "2023-01-01T00:00:00Z"

    def test_get_ksoft_ban_response_found_false(self):
        """Test GetKSoftBanResponse with found=False."""
        data = {"found": False}

        response = GetKSoftBanResponse(data)

        assert response.data == data
        assert response.found is False
        assert response.user_id is None
        assert response.tag is None
        assert response.reason is None
        assert response.proof is None
        assert response.moderator is None
        assert response.severe is None
        assert response.timestamp is None

    def test_get_ksoft_ban_response_partial_data(self):
        """Test GetKSoftBanResponse with partial data."""
        data = {
            "found": True,
            "id": "123456789",
            "tag": "TestUser#1234",
            "reason": "Test ban reason",
            # proof, moderator, severe, timestamp are missing
        }

        response = GetKSoftBanResponse(data)

        assert response.data == data
        assert response.found is True
        assert response.user_id == 123456789
        assert response.tag == "TestUser#1234"
        assert response.reason == "Test ban reason"
        assert response.proof is None
        assert response.moderator is None
        assert response.severe is None
        assert response.timestamp is None

    def test_get_ksoft_ban_response_string_integers(self):
        """Test GetKSoftBanResponse with string integers."""
        data = {
            "found": True,
            "id": "987654321",
            "moderator": "123456789",
            "severe": False,
        }

        response = GetKSoftBanResponse(data)

        assert response.data == data
        assert response.found is True
        assert response.user_id == 987654321
        assert response.moderator == 123456789
        assert response.severe is False

    def test_get_ksoft_ban_response_repr(self):
        """Test GetKSoftBanResponse repr."""
        data = {
            "found": True,
            "id": "123456789",
            "tag": "TestUser#1234",
            "reason": "Test ban reason",
            "proof": "https://example.com/proof",
            "moderator": "987654321",
            "severe": True,
            "timestamp": "2023-01-01T00:00:00Z",
        }

        response = GetKSoftBanResponse(data)
        repr_str = repr(response)

        assert "GetKSoftBanResponse" in repr_str
        assert "found=True" in repr_str
        assert "user_id=123456789" in repr_str
        assert "tag='TestUser#1234'" in repr_str

    def test_get_ksoft_ban_response_data_property(self):
        """Test GetKSoftBanResponse data property."""
        data = {
            "found": True,
            "id": "123456789",
        }

        response = GetKSoftBanResponse(data)

        assert response.data is data
        assert isinstance(response.data, dict)

    def test_get_ksoft_ban_response_properties_none_values(self):
        """Test GetKSoftBanResponse properties with None values."""
        data = {
            "found": True,
            # All optional fields are missing
        }

        response = GetKSoftBanResponse(data)

        assert response.found is True
        assert response.user_id is None
        assert response.tag is None
        assert response.reason is None
        assert response.proof is None
        assert response.moderator is None
        assert response.severe is None
        assert response.timestamp is None

    def test_get_ksoft_ban_response_slots(self):
        """Test GetKSoftBanResponse has proper slots."""
        data = {"found": False}

        response = GetKSoftBanResponse(data)

        assert hasattr(response, "__slots__")
        expected_slots = (
            "_data",
            "_found",
            "_user_id",
            "_tag",
            "_reason",
            "_proof",
            "_moderator",
            "_severe",
            "_timestamp",
        )
        assert response.__slots__ == expected_slots

    def test_get_ksoft_ban_response_empty_strings(self):
        """Test GetKSoftBanResponse with empty strings."""
        data = {
            "found": True,
            "id": "",
            "tag": "",
            "reason": "",
            "proof": "",
            "moderator": "",
            "timestamp": "",
        }

        response = GetKSoftBanResponse(data)

        assert response.found is True
        assert response.user_id is None  # Empty string becomes None
        assert response.tag == ""
        assert response.reason == ""
        assert response.proof == ""
        assert response.moderator is None  # Empty string becomes None
        assert response.timestamp == ""

    def test_get_ksoft_ban_response_complex_data(self):
        """Test GetKSoftBanResponse with complex data."""
        data = {
            "found": True,
            "id": "999999999",
            "tag": "ComplexUser#9999",
            "reason": "Complex ban reason with special chars: åäö",
            "proof": "https://example.com/proof?param=value&other=123",
            "moderator": "111111111",
            "severe": False,
            "timestamp": "2023-12-31T23:59:59Z",
        }

        response = GetKSoftBanResponse(data)

        assert response.data == data
        assert response.found is True
        assert response.user_id == 999999999
        assert response.tag == "ComplexUser#9999"
        assert response.reason == "Complex ban reason with special chars: åäö"
        assert response.proof == "https://example.com/proof?param=value&other=123"
        assert response.moderator == 111111111
        assert response.severe is False
        assert response.timestamp == "2023-12-31T23:59:59Z"

    def test_get_ksoft_ban_response_immutable_data(self):
        """Test GetKSoftBanResponse data is immutable reference."""
        data = {
            "found": True,
            "id": "123456789",
        }

        response = GetKSoftBanResponse(data)
        original_data = response.data

        # Modify original data
        data["found"] = False

        # Response data should reflect the change since it's a reference
        assert response.data["found"] is False
        assert response.data is original_data
