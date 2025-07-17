# Copyright 2022-Present GoogolGenius
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tokens models."""

from __future__ import annotations

from ravyapi.api.models.tokens import GetTokenResponse


class TestGetTokenResponse:
    """Test cases for the GetTokenResponse model."""

    def test_get_token_response_ravy_token(self) -> None:
        """Test GetTokenResponse with ravy token."""
        data = {
            "user": "123456789",
            "access": ["users", "avatars", "urls"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.user == 123456789
        assert response.access == ["users", "avatars", "urls"]
        assert response.application == 987654321
        assert response.token_type == "ravy"
        assert response.data == data

    def test_get_token_response_ksoft_token(self) -> None:
        """Test GetTokenResponse with ksoft token."""
        data = {
            "user": "987654321",
            "access": ["bans"],
            "application": 123456789,
            "type": "ksoft",
        }

        response = GetTokenResponse(data)

        assert response.user == 987654321
        assert response.access == ["bans"]
        assert response.application == 123456789
        assert response.token_type == "ksoft"
        assert response.data == data

    def test_get_token_response_empty_access(self) -> None:
        """Test GetTokenResponse with empty access list."""
        data: dict[str, str | list[str] | int] = {
            "user": "123456789",
            "access": [],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.access == []

    def test_get_token_response_string_integers(self) -> None:
        """Test GetTokenResponse converts string integers to int."""
        data = {
            "user": "123456789",
            "access": ["users"],
            "application": "987654321",
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.user == 123456789
        assert response.application == 987654321
        assert isinstance(response.user, int)
        assert isinstance(response.application, int)

    def test_get_token_response_repr(self) -> None:
        """Test GetTokenResponse __repr__ method."""
        data = {
            "user": "123456789",
            "access": ["users", "avatars"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)
        repr_str = repr(response)

        assert "GetTokenResponse" in repr_str
        assert "user=123456789" in repr_str
        assert "access=['users', 'avatars']" in repr_str
        assert "application=987654321" in repr_str
        assert "token_type='ravy'" in repr_str

    def test_get_token_response_data_property(self) -> None:
        """Test GetTokenResponse data property."""
        data = {
            "user": "123456789",
            "access": ["users"],
            "application": 987654321,
            "type": "ravy",
            "extra_field": "extra_value",
        }

        response = GetTokenResponse(data)

        assert response.data == data
        assert response.data is data  # Should be the same object

    def test_get_token_response_user_property(self) -> None:
        """Test GetTokenResponse user property."""
        data = {
            "user": "123456789",
            "access": ["users"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.user == 123456789
        assert isinstance(response.user, int)

    def test_get_token_response_access_property(self) -> None:
        """Test GetTokenResponse access property."""
        data = {
            "user": "123456789",
            "access": ["users", "avatars", "urls"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.access == ["users", "avatars", "urls"]
        assert isinstance(response.access, list)
        assert all(isinstance(perm, str) for perm in response.access)

    def test_get_token_response_application_property(self) -> None:
        """Test GetTokenResponse application property."""
        data = {
            "user": "123456789",
            "access": ["users"],
            "application": "987654321",
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.application == 987654321
        assert isinstance(response.application, int)

    def test_get_token_response_token_type_property(self) -> None:
        """Test GetTokenResponse token_type property."""
        ravy_data = {
            "user": "123456789",
            "access": ["users"],
            "application": 987654321,
            "type": "ravy",
        }

        ksoft_data = {
            "user": "123456789",
            "access": ["bans"],
            "application": 987654321,
            "type": "ksoft",
        }

        ravy_response = GetTokenResponse(ravy_data)
        ksoft_response = GetTokenResponse(ksoft_data)

        assert ravy_response.token_type == "ravy"
        assert ksoft_response.token_type == "ksoft"

    def test_get_token_response_slots(self) -> None:
        """Test GetTokenResponse has proper slots."""
        data = {
            "user": "123456789",
            "access": ["users"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        expected_slots = ("_data", "_user", "_access", "_application", "_token_type")
        assert response.__slots__ == expected_slots

    def test_get_token_response_complex_access(self) -> None:
        """Test GetTokenResponse with complex access permissions."""
        data = {
            "user": "123456789",
            "access": ["users.read", "users.write", "avatars.check", "admin.bans"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(data)

        assert response.access == [
            "users.read",
            "users.write",
            "avatars.check",
            "admin.bans",
        ]
        assert len(response.access) == 4

    def test_get_token_response_immutable_data(self) -> None:
        """Test GetTokenResponse data immutability."""
        original_data = {
            "user": "123456789",
            "access": ["users"],
            "application": 987654321,
            "type": "ravy",
        }

        response = GetTokenResponse(original_data)

        # Modifying original data should not affect response internal state
        original_data["user"] = "999999999"
        original_data["access"] = ["admin"]
        original_data["type"] = "ksoft"

        # Response should still have original values
        assert response.user == 123456789
        assert response.access == ["users"]
        assert response.token_type == "ravy"
        # But data property should reflect the changes since it's the same object
        assert response.data == original_data
