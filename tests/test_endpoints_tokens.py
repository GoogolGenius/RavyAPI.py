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
"""Tests for the tokens endpoint."""

from __future__ import annotations

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from ravyapi.api.endpoints.tokens import Tokens
from ravyapi.api.models.tokens import GetTokenResponse
from ravyapi.http import HTTPAwareEndpoint


class TestTokens:
    """Test cases for the Tokens endpoint."""

    @pytest.fixture
    def mock_http_client(self) -> MagicMock:
        """Create a mock HTTP client."""
        mock = MagicMock()
        mock.get = AsyncMock()
        mock.get_permissions = AsyncMock()
        mock.permissions = ["tokens"]
        mock.paths = MagicMock()
        mock.paths.tokens = MagicMock()
        mock.paths.tokens.route = "/tokens/@current"
        return mock

    @pytest.fixture
    def tokens_endpoint(self, mock_http_client: MagicMock) -> Tokens:
        """Create a Tokens endpoint instance."""
        return Tokens(mock_http_client)

    def test_tokens_initialization(self, mock_http_client: MagicMock) -> None:
        """Test Tokens endpoint initialization."""
        tokens = Tokens(mock_http_client)
        assert tokens._http is mock_http_client  # type: ignore
        assert isinstance(tokens, HTTPAwareEndpoint)

    def test_tokens_slots(self, tokens_endpoint: Tokens) -> None:
        """Test Tokens has proper slots."""
        assert tokens_endpoint.__slots__ == ()

    @pytest.mark.asyncio
    async def test_get_token_success(self, tokens_endpoint: Tokens) -> None:
        """Test get_token method success."""
        mock_response = {
            "user": "123456789",
            "access": ["users", "avatars", "urls"],
            "application": 987654321,
            "type": "ravy",
        }

        tokens_endpoint._http.get.return_value = mock_response  # type: ignore

        result = await tokens_endpoint.get_token()

        assert isinstance(result, GetTokenResponse)
        assert result.user == 123456789
        assert result.access == ["users", "avatars", "urls"]
        assert result.application == 987654321
        assert result.token_type == "ravy"

        tokens_endpoint._http.get.assert_called_once_with("/tokens/@current")  # type: ignore

    @pytest.mark.asyncio
    async def test_get_token_ksoft_type(self, tokens_endpoint: Tokens) -> None:
        """Test get_token with ksoft token type."""
        mock_response = {
            "user": "987654321",
            "access": ["bans"],
            "application": 123456789,
            "type": "ksoft",
        }

        tokens_endpoint._http.get.return_value = mock_response  # type: ignore

        result = await tokens_endpoint.get_token()

        assert isinstance(result, GetTokenResponse)
        assert result.user == 987654321
        assert result.access == ["bans"]
        assert result.application == 123456789
        assert result.token_type == "ksoft"

    @pytest.mark.asyncio
    async def test_get_token_empty_access(self, tokens_endpoint: Tokens) -> None:
        """Test get_token with empty access list."""
        mock_response: dict[str, Any] = {
            "user": "123456789",
            "access": [],
            "application": 987654321,
            "type": "ravy",
        }

        tokens_endpoint._http.get.return_value = mock_response  # type: ignore

        result = await tokens_endpoint.get_token()

        assert isinstance(result, GetTokenResponse)
        assert result.access == []

    @pytest.mark.asyncio
    async def test_get_token_no_permission_check(self, tokens_endpoint: Tokens) -> None:
        """Test get_token doesn't require permission check."""
        mock_response = {
            "user": "123456789",
            "access": ["users"],
            "application": 987654321,
            "type": "ravy",
        }

        tokens_endpoint._http.get.return_value = mock_response  # type: ignore

        await tokens_endpoint.get_token()

        # Verify no permission check was called (tokens endpoint doesn't use @with_permission_check)
        tokens_endpoint._http.get_permissions.assert_not_called()  # type: ignore
