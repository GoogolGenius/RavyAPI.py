"""Fixtures for tests."""

from __future__ import annotations

from typing import Any, Generator
from unittest.mock import AsyncMock

import pytest
from aioresponses import aioresponses

from ravyapi.api.endpoints import Avatars, Guilds, KSoft, Tokens, URLs, Users
from ravyapi.client import Client
from ravyapi.http import HTTPClient


@pytest.fixture
def valid_ravy_token() -> str:
    """Valid Ravy token for testing."""
    return "abcdefghijklmnopqrstuvwx.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"


@pytest.fixture
def valid_ksoft_token() -> str:
    """Valid KSoft token for testing."""
    return "1234567890abcdef1234567890abcdef12345678"


@pytest.fixture
def invalid_token() -> str:
    """Invalid token for testing."""
    return "invalid_token"


@pytest.fixture
def sample_check_avatar_response():
    """Sample check avatar response."""
    return {
        "matched": True,
        "key": "test_key",
        "similarity": 0.95,
    }


@pytest.fixture
def sample_get_token_response():
    """Sample get token response."""
    return {
        "user": 12345,
        "access": ["users", "avatars", "urls"],
        "application": 67890,
        "token_type": "ravy",
    }


@pytest.fixture
def mock_aioresponses() -> Generator[aioresponses, Any, None]:
    """Mock aioresponses fixture."""
    with aioresponses() as m:
        yield m


@pytest.fixture
def mock_http_client(valid_ravy_token: str) -> HTTPClient:
    """Mock HTTPClient for testing."""
    # Create a mock session to avoid the event loop issue
    mock_session = AsyncMock()
    client = HTTPClient.__new__(HTTPClient)
    client._token = valid_ravy_token  # type: ignore
    client._permissions = None  # type: ignore
    client._phisherman_token = None  # type: ignore
    client._headers = {  # type: ignore
        "Authorization": valid_ravy_token,
        "User-Agent": "Test-Agent",
    }
    client._session = mock_session  # type: ignore
    return client


@pytest.fixture
def mock_client(valid_ravy_token: str, mock_http_client: HTTPClient) -> Client:
    """Mock Client for testing."""
    client = Client.__new__(Client)
    client._token = valid_ravy_token  # type: ignore
    client._http = mock_http_client  # type: ignore
    client._closed = False  # type: ignore
    client._avatars = Avatars(mock_http_client)  # type: ignore
    client._guilds = Guilds(mock_http_client)  # type: ignore
    client._ksoft = KSoft(mock_http_client)  # type: ignore
    client._users = Users(mock_http_client)  # type: ignore
    client._urls = URLs(mock_http_client)  # type: ignore
    client._tokens = Tokens(mock_http_client)  # type: ignore
    return client


@pytest.fixture
def mock_avatars_endpoint(mock_http_client: HTTPClient) -> Avatars:
    """Mock Avatars endpoint for testing."""
    return Avatars(mock_http_client)


@pytest.fixture
def mock_tokens_endpoint(mock_http_client: HTTPClient) -> Tokens:
    """Mock Tokens endpoint for testing."""
    return Tokens(mock_http_client)


@pytest.fixture
def sample_get_guild_response():
    """Sample get guild response."""
    return {
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


@pytest.fixture
def sample_get_user_response():
    """Sample get user response."""
    return {
        "pronouns": "he/him",
        "trust": {"level": 3, "label": "Neutral"},
        "whitelists": [
            {"provider": "ravy", "reason": "Test whitelist", "moderator": "987654321"}
        ],
        "bans": [
            {
                "provider": "ravy",
                "reason": "Test ban",
                "moderator": "987654321",
                "reason_key": "test_key",
            }
        ],
        "rep": [{"provider": "ravy", "reputation": 100, "moderator": "987654321"}],
        "sentinel": {
            "tracked": True,
            "reason": "Test sentinel",
            "moderator": "987654321",
        },
    }


@pytest.fixture
def sample_get_website_response():
    """Sample get website response."""
    return {
        "is_fraudulent": False,
        "message": "Safe website",
        "scan_date": "2023-01-01T00:00:00Z",
    }


@pytest.fixture
def sample_get_ksoft_ban_response():
    """Sample get KSoft ban response."""
    return {
        "banned": True,
        "reason": "Test ban reason",
        "moderator": "987654321",
        "appeal": "https://example.com/appeal",
        "date": "2023-01-01T00:00:00Z",
    }


@pytest.fixture
def mock_guilds_endpoint(mock_http_client: HTTPClient) -> Guilds:
    """Mock Guilds endpoint for testing."""
    return Guilds(mock_http_client)


@pytest.fixture
def mock_users_endpoint(mock_http_client: HTTPClient) -> Users:
    """Mock Users endpoint for testing."""
    return Users(mock_http_client)


@pytest.fixture
def mock_urls_endpoint(mock_http_client: HTTPClient) -> URLs:
    """Mock URLs endpoint for testing."""
    return URLs(mock_http_client)


@pytest.fixture
def mock_ksoft_endpoint(mock_http_client: HTTPClient) -> KSoft:
    """Mock KSoft endpoint for testing."""
    return KSoft(mock_http_client)
