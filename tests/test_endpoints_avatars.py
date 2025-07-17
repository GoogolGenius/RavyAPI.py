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
"""Tests for the avatars endpoint."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ravyapi.api.endpoints.avatars import Avatars
from ravyapi.api.models.avatars import CheckAvatarResponse
from ravyapi.http import HTTPAwareEndpoint


class TestAvatars:
    """Test cases for the Avatars endpoint."""

    @pytest.fixture
    def mock_http_client(self) -> MagicMock:
        """Create a mock HTTP client."""
        mock = MagicMock()
        mock.get = AsyncMock()
        mock.post = AsyncMock()
        mock.get_permissions = AsyncMock()
        mock.permissions = ["avatars"]
        mock.paths = MagicMock()
        mock.paths.avatars = MagicMock()
        mock.paths.avatars.route = "/avatars"
        return mock

    @pytest.fixture
    def avatars_endpoint(self, mock_http_client: MagicMock) -> Avatars:
        """Create an Avatars endpoint instance."""
        return Avatars(mock_http_client)

    def test_avatars_initialization(self, mock_http_client: MagicMock) -> None:
        """Test Avatars endpoint initialization."""
        avatars = Avatars(mock_http_client)
        assert avatars._http is mock_http_client  # type: ignore
        assert isinstance(avatars, HTTPAwareEndpoint)

    def test_avatars_slots(self, avatars_endpoint: Avatars) -> None:
        """Test Avatars has proper slots."""
        assert avatars_endpoint.__slots__ == ()

    @pytest.mark.asyncio
    async def test_check_avatar_with_url_success(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with URL string."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"
        threshold = 0.95
        method = "phash"

        mock_response = {"matched": True, "key": "avatar_key_123", "similarity": 0.98}

        avatars_endpoint._http.get.return_value = mock_response  # type: ignore

        result = await avatars_endpoint.check_avatar(avatar_url, threshold, method)

        assert isinstance(result, CheckAvatarResponse)
        avatars_endpoint._http.get.assert_called_once_with(  # type: ignore
            "/avatars",
            params={
                "avatar": avatar_url,
                "threshold": threshold,
                "method": method,
            },
        )

    @pytest.mark.asyncio
    async def test_check_avatar_with_bytes_success(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with bytes data."""
        avatar_bytes = b"fake_avatar_data"
        threshold = 0.97
        method = "ssim"

        mock_response = {"matched": False, "key": None, "similarity": None}

        avatars_endpoint._http.post.return_value = mock_response  # type: ignore

        with patch("aiohttp.FormData") as mock_form_data:
            mock_form = MagicMock()
            mock_form_data.return_value = mock_form

            result = await avatars_endpoint.check_avatar(
                avatar_bytes, threshold, method
            )

            assert isinstance(result, CheckAvatarResponse)
            mock_form.add_field.assert_called_once_with(
                "avatar", avatar_bytes, content_type="application/octet-stream"
            )
            avatars_endpoint._http.post.assert_called_once_with(  # type: ignore
                "/avatars",
                params={
                    "threshold": threshold,
                    "method": method,
                },
                data=mock_form,
            )

    @pytest.mark.asyncio
    async def test_check_avatar_default_parameters(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with default parameters."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        mock_response = {"matched": True, "key": "avatar_key_123", "similarity": 0.98}

        avatars_endpoint._http.get.return_value = mock_response  # type: ignore

        result = await avatars_endpoint.check_avatar(avatar_url)

        assert isinstance(result, CheckAvatarResponse)
        avatars_endpoint._http.get.assert_called_once_with(  # type: ignore
            "/avatars",
            params={
                "avatar": avatar_url,
                "threshold": 0.97,  # default
                "method": "phash",  # default
            },
        )

    @pytest.mark.asyncio
    async def test_check_avatar_invalid_avatar_type(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with invalid avatar type."""
        with pytest.raises(
            TypeError, match='Parameter "avatar" must be of type "str" or "bytes"'
        ):
            await avatars_endpoint.check_avatar(123)  # type: ignore

    @pytest.mark.asyncio
    async def test_check_avatar_empty_avatar_string(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with empty avatar string."""
        with pytest.raises(ValueError, match='Parameter "avatar" must not be empty'):
            await avatars_endpoint.check_avatar("")

    @pytest.mark.asyncio
    async def test_check_avatar_empty_avatar_bytes(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with empty avatar bytes."""
        with pytest.raises(ValueError, match='Parameter "avatar" must not be empty'):
            await avatars_endpoint.check_avatar(b"")

    @pytest.mark.asyncio
    async def test_check_avatar_invalid_threshold_low(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with threshold too low."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        with pytest.raises(
            ValueError,
            match='Parameter "threshold" must be of type "float" between 0 and 1',
        ):
            await avatars_endpoint.check_avatar(avatar_url, threshold=-0.1)

    @pytest.mark.asyncio
    async def test_check_avatar_invalid_threshold_high(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with threshold too high."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        with pytest.raises(
            ValueError,
            match='Parameter "threshold" must be of type "float" between 0 and 1',
        ):
            await avatars_endpoint.check_avatar(avatar_url, threshold=1.1)

    @pytest.mark.asyncio
    async def test_check_avatar_invalid_method(self, avatars_endpoint: Avatars) -> None:
        """Test check_avatar with invalid method."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        with pytest.raises(
            ValueError, match='Parameter "method" must be either "ssim" or "phash"'
        ):
            await avatars_endpoint.check_avatar(avatar_url, method="invalid")  # type: ignore

    @pytest.mark.asyncio
    async def test_check_avatar_invalid_url_hostname(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with invalid URL hostname."""
        invalid_url = "https://example.com/avatar.png"

        with pytest.raises(
            ValueError,
            match='Parameter "avatar_url" must start with "https://cdn.discordapp.com"',
        ):
            await avatars_endpoint.check_avatar(invalid_url)

    @pytest.mark.asyncio
    async def test_check_avatar_valid_url_variations(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with various valid URL formats."""
        valid_urls = [
            "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png",
            "https://cdn.discordapp.com/avatars/123456789/avatar_hash.jpg",
            "https://cdn.discordapp.com/avatars/123456789/avatar_hash.gif",
            "https://cdn.discordapp.com/avatars/123456789/avatar_hash.webp",
        ]

        mock_response = {"matched": True, "key": "avatar_key_123", "similarity": 0.98}

        avatars_endpoint._http.get.return_value = mock_response  # type: ignore

        for url in valid_urls:
            result = await avatars_endpoint.check_avatar(url)
            assert isinstance(result, CheckAvatarResponse)

    @pytest.mark.asyncio
    async def test_check_avatar_boundary_threshold_values(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar with boundary threshold values."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        mock_response = {"matched": True, "key": "avatar_key_123", "similarity": 0.98}

        avatars_endpoint._http.get.return_value = mock_response  # type: ignore

        # Test boundary values
        for threshold in [0.0, 1.0]:
            result = await avatars_endpoint.check_avatar(
                avatar_url, threshold=threshold
            )
            assert isinstance(result, CheckAvatarResponse)

    @pytest.mark.asyncio
    async def test_check_avatar_both_methods(self, avatars_endpoint: Avatars) -> None:
        """Test check_avatar with both supported methods."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        mock_response = {"matched": True, "key": "avatar_key_123", "similarity": 0.98}

        avatars_endpoint._http.get.return_value = mock_response  # type: ignore

        for method in ["ssim", "phash"]:
            result = await avatars_endpoint.check_avatar(avatar_url, method=method)  # type: ignore
            assert isinstance(result, CheckAvatarResponse)

    @pytest.mark.asyncio
    async def test_check_avatar_permission_check(
        self, avatars_endpoint: Avatars
    ) -> None:
        """Test check_avatar calls permission check."""
        avatar_url = "https://cdn.discordapp.com/avatars/123456789/avatar_hash.png"

        mock_response = {"matched": True, "key": "avatar_key_123", "similarity": 0.98}

        avatars_endpoint._http.get.return_value = mock_response  # type: ignore

        await avatars_endpoint.check_avatar(avatar_url)

        # Verify permission check was called
        avatars_endpoint._http.get_permissions.assert_called_once()  # type: ignore
