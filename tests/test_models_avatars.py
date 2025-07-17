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
"""Tests for avatars models."""

from __future__ import annotations

from ravyapi.api.models.avatars import CheckAvatarResponse


class TestCheckAvatarResponse:
    """Test cases for the CheckAvatarResponse model."""

    def test_check_avatar_response_matched_true(self) -> None:
        """Test CheckAvatarResponse with matched avatar."""
        data = {"matched": True, "key": "avatar_key_123", "similarity": 0.95}

        response = CheckAvatarResponse(data)

        assert response.matched is True
        assert response.key == "avatar_key_123"
        assert response.similarity == 0.95
        assert response.data == data

    def test_check_avatar_response_matched_false(self) -> None:
        """Test CheckAvatarResponse with unmatched avatar."""
        data = {"matched": False, "key": None, "similarity": None}

        response = CheckAvatarResponse(data)

        assert response.matched is False
        assert response.key is None
        assert response.similarity is None
        assert response.data == data

    def test_check_avatar_response_missing_optional_fields(self) -> None:
        """Test CheckAvatarResponse with missing optional fields."""
        data = {"matched": False}

        response = CheckAvatarResponse(data)

        assert response.matched is False
        assert response.key is None
        assert response.similarity is None
        assert response.data == data

    def test_check_avatar_response_partial_data(self) -> None:
        """Test CheckAvatarResponse with partial data."""
        data = {
            "matched": True,
            "key": "avatar_key_456",
            # similarity missing
        }

        response = CheckAvatarResponse(data)

        assert response.matched is True
        assert response.key == "avatar_key_456"
        assert response.similarity is None
        assert response.data == data

    def test_check_avatar_response_repr(self) -> None:
        """Test CheckAvatarResponse __repr__ method."""
        data = {"matched": True, "key": "avatar_key_123", "similarity": 0.95}

        response = CheckAvatarResponse(data)
        repr_str = repr(response)

        assert "CheckAvatarResponse" in repr_str
        assert "matched=True" in repr_str
        assert "key='avatar_key_123'" in repr_str
        assert "similarity=0.95" in repr_str

    def test_check_avatar_response_repr_none_values(self) -> None:
        """Test CheckAvatarResponse __repr__ with None values."""
        data = {"matched": False, "key": None, "similarity": None}

        response = CheckAvatarResponse(data)
        repr_str = repr(response)

        assert "CheckAvatarResponse" in repr_str
        assert "matched=False" in repr_str
        assert "key=None" in repr_str
        assert "similarity=None" in repr_str

    def test_check_avatar_response_data_property(self) -> None:
        """Test CheckAvatarResponse data property."""
        data = {
            "matched": True,
            "key": "avatar_key_123",
            "similarity": 0.95,
            "extra_field": "extra_value",
        }

        response = CheckAvatarResponse(data)

        assert response.data == data
        assert response.data is data  # Should be the same object

    def test_check_avatar_response_matched_property(self) -> None:
        """Test CheckAvatarResponse matched property."""
        data = {"matched": True}
        response = CheckAvatarResponse(data)
        assert response.matched is True

        data = {"matched": False}
        response = CheckAvatarResponse(data)
        assert response.matched is False

    def test_check_avatar_response_key_property(self) -> None:
        """Test CheckAvatarResponse key property."""
        data = {"matched": True, "key": "test_key"}
        response = CheckAvatarResponse(data)
        assert response.key == "test_key"

        data = {"matched": False}
        response = CheckAvatarResponse(data)
        assert response.key is None

    def test_check_avatar_response_similarity_property(self) -> None:
        """Test CheckAvatarResponse similarity property."""
        data = {"matched": True, "similarity": 0.85}
        response = CheckAvatarResponse(data)
        assert response.similarity == 0.85

        data = {"matched": False}
        response = CheckAvatarResponse(data)
        assert response.similarity is None

    def test_check_avatar_response_similarity_edge_cases(self) -> None:
        """Test CheckAvatarResponse similarity with edge case values."""
        # Test with 0.0 similarity
        data = {"matched": True, "similarity": 0.0}
        response = CheckAvatarResponse(data)
        assert response.similarity == 0.0

        # Test with 1.0 similarity
        data = {"matched": True, "similarity": 1.0}
        response = CheckAvatarResponse(data)
        assert response.similarity == 1.0

    def test_check_avatar_response_slots(self) -> None:
        """Test CheckAvatarResponse has proper slots."""
        data = {"matched": True}
        response = CheckAvatarResponse(data)

        expected_slots = ("_data", "_matched", "_key", "_similarity")
        assert response.__slots__ == expected_slots

    def test_check_avatar_response_complex_data(self) -> None:
        """Test CheckAvatarResponse with complex data structure."""
        data = {
            "matched": True,
            "key": "avatar_key_123",
            "similarity": 0.95,
            "metadata": {
                "algorithm": "phash",
                "threshold": 0.97,
                "processed_at": "2023-01-01T00:00:00Z",
            },
            "additional_info": ["info1", "info2"],
        }

        response = CheckAvatarResponse(data)

        assert response.matched is True
        assert response.key == "avatar_key_123"
        assert response.similarity == 0.95
        assert response.data == data
        assert response.data["metadata"]["algorithm"] == "phash"
        assert response.data["additional_info"] == ["info1", "info2"]

    def test_check_avatar_response_immutable_data(self) -> None:
        """Test CheckAvatarResponse data immutability."""
        original_data = {"matched": True, "key": "avatar_key_123", "similarity": 0.95}

        response = CheckAvatarResponse(original_data)

        # Modifying original data should not affect response
        original_data["matched"] = False
        original_data["key"] = "modified_key"

        # Response should still have original values
        assert response.matched is True
        assert response.key == "avatar_key_123"
        assert response.similarity == 0.95
