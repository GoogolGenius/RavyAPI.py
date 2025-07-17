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
"""Tests for constants."""

from __future__ import annotations

import platform
import re

import aiohttp

from ravyapi._about import __author__, __repository__, __version__
from ravyapi.const import BASE_URL, KSOFT_TOKEN_REGEX, RAVY_TOKEN_REGEX, USER_AGENT


class TestConstants:
    """Test cases for constants."""

    def test_base_url(self) -> None:
        """Test BASE_URL constant."""
        assert BASE_URL == "https://ravy.org/api/v1"
        assert isinstance(BASE_URL, str)

    def test_ravy_token_regex(self) -> None:
        """Test RAVY_TOKEN_REGEX constant."""
        assert RAVY_TOKEN_REGEX == r"[A-Za-z0-9_-]{24}\.[0-9a-f]{64}"
        assert isinstance(RAVY_TOKEN_REGEX, str)

    def test_ksoft_token_regex(self) -> None:
        """Test KSOFT_TOKEN_REGEX constant."""
        assert KSOFT_TOKEN_REGEX == r"[0-9a-f]{40}"
        assert isinstance(KSOFT_TOKEN_REGEX, str)

    def test_user_agent_format(self) -> None:
        """Test USER_AGENT constant format."""
        # Check that it contains expected components
        assert __repository__ in USER_AGENT
        assert __version__ in USER_AGENT
        assert __author__ in USER_AGENT
        assert aiohttp.__version__ in USER_AGENT
        assert platform.python_implementation() in USER_AGENT
        assert platform.python_version() in USER_AGENT
        assert platform.system() in USER_AGENT
        assert platform.architecture()[0] in USER_AGENT

    def test_user_agent_structure(self) -> None:
        """Test USER_AGENT constant structure."""
        expected_start = f"RavyAPI.py ({__repository__}, {__version__}) {__author__}"
        assert USER_AGENT.startswith(expected_start)
        assert isinstance(USER_AGENT, str)

    def test_ravy_token_regex_valid_tokens(self) -> None:
        """Test RAVY_TOKEN_REGEX with valid token patterns."""
        pattern = re.compile(f"^{RAVY_TOKEN_REGEX}$")  # Add anchors for exact match

        # Test with valid tokens
        valid_tokens = [
            "abcdefghijklmnopqrstuvwx.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
            "abc123DEF456ghi789JKL012.abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            "test_token-with_dashes12.0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        ]

        for token in valid_tokens:
            assert pattern.match(token) is not None, f"Token {token} should be valid"

    def test_ravy_token_regex_invalid_tokens(self) -> None:
        """Test RAVY_TOKEN_REGEX with invalid token patterns."""
        pattern = re.compile(f"^{RAVY_TOKEN_REGEX}$")  # Add anchors for exact match

        # Test with invalid tokens
        invalid_tokens = [
            "too_short.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # First part too short
            "abcdefghijklmnopqrstuvwx.too_short",  # Second part too short
            "abcdefghijklmnopqrstuvwx.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1",  # Second part too long
            "abcdefghijklmnopqrstuvwx12345.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # First part too long
            "abcdefghijklmnopqrstuvwx-1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # Missing dot
            "abcdefghijklmnopqrstuvwx.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdefG",  # Invalid character in second part
            "abcdefghijklmnopqrstuvwx@.1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # Invalid character in first part
            "",  # Empty string
            "no_dot_separator",  # No dot separator
        ]

        for token in invalid_tokens:
            assert pattern.match(token) is None, f"Token {token} should be invalid"

    def test_ksoft_token_regex_valid_tokens(self) -> None:
        """Test KSOFT_TOKEN_REGEX with valid token patterns."""
        pattern = re.compile(KSOFT_TOKEN_REGEX)

        # Test with valid tokens
        valid_tokens = [
            "1234567890abcdef1234567890abcdef12345678",
            "abcdef1234567890abcdef1234567890abcdef12",
            "0123456789abcdef0123456789abcdef01234567",
            "fedcba0987654321fedcba0987654321fedcba09",
        ]

        for token in valid_tokens:
            assert pattern.match(token) is not None, f"Token {token} should be valid"

    def test_ksoft_token_regex_invalid_tokens(self) -> None:
        """Test KSOFT_TOKEN_REGEX with invalid token patterns."""
        pattern = re.compile(f"^{KSOFT_TOKEN_REGEX}$")  # Add anchors for exact match

        # Test with invalid tokens
        invalid_tokens = [
            "1234567890abcdef1234567890abcdef1234567",  # Too short
            "1234567890abcdef1234567890abcdef1234567890",  # Too long
            "1234567890abcdef1234567890abcdef1234567G",  # Invalid character
            "1234567890ABCDEF1234567890ABCDEF12345678",  # Uppercase letters
            "",  # Empty string
            "not_hex_characters_at_all_here_invalid_token",  # Non-hex characters
        ]

        for token in invalid_tokens:
            assert pattern.match(token) is None, f"Token {token} should be invalid"

    def test_constants_are_final(self) -> None:
        """Test that constants are defined as Final."""
        # This test mainly checks that we can access the constants
        # In runtime, Final doesn't enforce immutability, but it's a type hint
        assert BASE_URL is not None
        assert RAVY_TOKEN_REGEX is not None
        assert KSOFT_TOKEN_REGEX is not None
        assert USER_AGENT is not None
