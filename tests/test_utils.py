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
"""Tests for utility functions."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from ravyapi.api.errors import AccessError
from ravyapi.http import HTTPAwareEndpoint
from ravyapi.utils import has_permissions, with_permission_check


class TestHasPermissions:
    """Test cases for the has_permissions function."""

    def test_has_permissions_exact_match(self) -> None:
        """Test has_permissions with exact permission match."""
        required = "users.read"
        permissions = ["users.read", "avatars.check"]

        assert has_permissions(required, permissions) is True

    def test_has_permissions_parent_match(self) -> None:
        """Test has_permissions with parent permission match."""
        required = "users.read.profile"
        permissions = ["users.read", "avatars.check"]

        assert has_permissions(required, permissions) is True

    def test_has_permissions_grandparent_match(self) -> None:
        """Test has_permissions with grandparent permission match."""
        required = "users.read.profile.detailed"
        permissions = ["users", "avatars.check"]

        assert has_permissions(required, permissions) is True

    def test_has_permissions_no_match(self) -> None:
        """Test has_permissions with no permission match."""
        required = "users.read"
        permissions = ["avatars.check", "urls.scan"]

        assert has_permissions(required, permissions) is False

    def test_has_permissions_empty_permissions(self) -> None:
        """Test has_permissions with empty permissions list."""
        required = "users.read"
        permissions: list[str] = []

        assert has_permissions(required, permissions) is False

    def test_has_permissions_empty_required(self) -> None:
        """Test has_permissions with empty required permission."""
        required = ""
        permissions = ["users.read", "avatars.check"]

        assert has_permissions(required, permissions) is False

    def test_has_permissions_partial_match_no_permission(self) -> None:
        """Test has_permissions with partial match that doesn't grant permission."""
        required = "users.read"
        permissions = ["users.write", "avatars.check"]

        assert has_permissions(required, permissions) is False

    def test_has_permissions_single_level_match(self) -> None:
        """Test has_permissions with single level permission."""
        required = "users"
        permissions = ["users", "avatars"]

        assert has_permissions(required, permissions) is True

    def test_has_permissions_complex_hierarchy(self) -> None:
        """Test has_permissions with complex permission hierarchy."""
        required = "admin.users.bans.create"
        permissions = ["admin.users", "regular.users.read"]

        assert has_permissions(required, permissions) is True

    def test_has_permissions_case_sensitive(self) -> None:
        """Test has_permissions is case sensitive."""
        required = "Users.Read"
        permissions = ["users.read", "avatars.check"]

        assert has_permissions(required, permissions) is False


class TestWithPermissionCheck:
    """Test cases for the with_permission_check decorator."""

    @pytest.mark.asyncio
    async def test_with_permission_check_success(self) -> None:
        """Test with_permission_check decorator with sufficient permissions."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = ["users.read", "avatars.check"]

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("users.read")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            return "success"

        result = await test_method(mock_endpoint)
        assert result == "success"
        mock_http.get_permissions.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_permission_check_insufficient_permissions(self) -> None:
        """Test with_permission_check decorator with insufficient permissions."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = ["avatars.check"]

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("users.read")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            return "success"

        with pytest.raises(AccessError) as exc_info:
            await test_method(mock_endpoint)

        assert exc_info.value.required == "users.read"
        mock_http.get_permissions.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_permission_check_none_permissions(self) -> None:
        """Test with_permission_check decorator when permissions are None."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = None

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("users.read")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            return "success"

        with pytest.raises(AssertionError, match='Permissions is "None"'):
            await test_method(mock_endpoint)

        mock_http.get_permissions.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_permission_check_parent_permission(self) -> None:
        """Test with_permission_check decorator with parent permission."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = ["users", "avatars.check"]

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("users.read.profile")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            return "success"

        result = await test_method(mock_endpoint)
        assert result == "success"
        mock_http.get_permissions.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_permission_check_with_args_and_kwargs(self) -> None:
        """Test with_permission_check decorator with method arguments."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = ["users.read"]

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("users.read")
        async def test_method(
            self: HTTPAwareEndpoint, user_id: int, *, param: str = "default"
        ) -> str:
            return f"success-{user_id}-{param}"

        result = await test_method(mock_endpoint, 123, param="test")
        assert result == "success-123-test"
        mock_http.get_permissions.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_permission_check_preserves_function_metadata(self) -> None:
        """Test with_permission_check decorator preserves function metadata."""

        @with_permission_check("users.read")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            """Test method docstring."""
            return "success"

        assert test_method.__name__ == "test_method"
        assert test_method.__doc__ == "Test method docstring."

    @pytest.mark.asyncio
    async def test_with_permission_check_multiple_decorators(self) -> None:
        """Test with_permission_check decorator with multiple permission checks."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = ["users.read", "admin.users"]

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("admin.users")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            return "success"

        result = await test_method(mock_endpoint)
        assert result == "success"
        mock_http.get_permissions.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_permission_check_exception_propagation(self) -> None:
        """Test with_permission_check decorator propagates exceptions from decorated method."""
        mock_http = MagicMock()
        mock_http.get_permissions = AsyncMock()
        mock_http.permissions = ["users.read"]

        mock_endpoint = MagicMock(spec=HTTPAwareEndpoint)
        mock_endpoint._http = mock_http

        @with_permission_check("users.read")
        async def test_method(self: HTTPAwareEndpoint) -> str:
            raise ValueError("Test exception")

        with pytest.raises(ValueError, match="Test exception"):
            await test_method(mock_endpoint)

        mock_http.get_permissions.assert_called_once()
