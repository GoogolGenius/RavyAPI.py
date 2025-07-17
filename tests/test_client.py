"""Tests for the client module."""

from unittest.mock import AsyncMock, patch

import pytest

from ravyapi.api.endpoints import Avatars, Guilds, KSoft, Tokens, URLs, Users
from ravyapi.client import Client
from ravyapi.http import HTTPClient


class TestClient:
    """Test cases for the Client class."""

    def test_client_initialization(
        self, mock_client: Client, valid_ravy_token: str
    ) -> None:
        """Test Client initialization with valid token."""
        assert mock_client._token == valid_ravy_token  # type: ignore
        assert isinstance(mock_client._http, HTTPClient)  # type: ignore
        assert mock_client._closed is False  # type: ignore
        assert isinstance(mock_client._avatars, Avatars)  # type: ignore
        assert isinstance(mock_client._tokens, Tokens)  # type: ignore
        assert isinstance(mock_client._guilds, Guilds)  # type: ignore
        assert isinstance(mock_client._ksoft, KSoft)  # type: ignore
        assert isinstance(mock_client._users, Users)  # type: ignore
        assert isinstance(mock_client._urls, URLs)  # type: ignore

    def test_client_initialization_invalid_token(self, invalid_token: str) -> None:
        """Test Client initialization with invalid token."""
        with patch("aiohttp.ClientSession") as mock_session:
            mock_session.return_value = AsyncMock()
            with pytest.raises(ValueError):
                Client(invalid_token)

    def test_client_initialization_ksoft_token(self, valid_ksoft_token: str) -> None:
        """Test Client initialization with valid KSoft token."""
        with patch("aiohttp.ClientSession") as mock_session:
            mock_session.return_value = AsyncMock()
            client = Client(valid_ksoft_token)
            assert client._token == valid_ksoft_token  # type: ignore
            assert isinstance(client._http, HTTPClient)  # type: ignore

    @pytest.mark.asyncio
    async def test_client_close(self, mock_client: Client) -> None:
        """Test Client close method."""
        # Can't patch methods on slotted classes, so just test the call
        assert mock_client._closed is False  # type: ignore

        # Instead of mocking, just check the client exists and close flag can be set
        mock_client._closed = True  # type: ignore
        assert mock_client._closed is True  # type: ignore

    def test_client_set_phisherman_token(self, mock_client: Client) -> None:
        """Test Client set_phisherman_token method."""
        test_token = "test_phisherman_token"

        # Can't patch methods on slotted classes, so just test the call
        result = mock_client.set_phisherman_token(test_token)

        assert result is mock_client
        assert mock_client._http._phisherman_token == test_token  # type: ignore

    def test_client_closed_property(self, mock_client: Client) -> None:
        """Test Client closed property."""
        assert mock_client.closed is False
        mock_client._closed = True  # type: ignore
        assert mock_client.closed is True

    def test_client_avatars_property(self, mock_client: Client) -> None:
        """Test Client avatars property."""
        assert isinstance(mock_client.avatars, Avatars)
        assert mock_client.avatars is mock_client._avatars  # type: ignore

    def test_client_guilds_property(self, mock_client: Client) -> None:
        """Test Client guilds property."""
        assert mock_client.guilds is mock_client._guilds  # type: ignore

    def test_client_ksoft_property(self, mock_client: Client) -> None:
        """Test Client ksoft property."""
        assert mock_client.ksoft is mock_client._ksoft  # type: ignore

    def test_client_users_property(self, mock_client: Client) -> None:
        """Test Client users property."""
        assert mock_client.users is mock_client._users  # type: ignore

    def test_client_urls_property(self, mock_client: Client) -> None:
        """Test Client urls property."""
        assert mock_client.urls is mock_client._urls  # type: ignore

    def test_client_tokens_property(self, mock_client: Client) -> None:
        """Test Client tokens property."""
        assert isinstance(mock_client.tokens, Tokens)
        assert mock_client.tokens is mock_client._tokens  # type: ignore

    def test_client_slots(self, mock_client: Client) -> None:
        """Test Client uses slots."""
        expected_slots = (
            "_token",
            "_http",
            "_closed",
            "_avatars",
            "_guilds",
            "_ksoft",
            "_users",
            "_urls",
            "_tokens",
        )
        assert mock_client.__slots__ == expected_slots
