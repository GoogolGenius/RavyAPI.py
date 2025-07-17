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
"""Tests for package metadata."""

from __future__ import annotations

from ravyapi._about import (
    __all__,
    __author__,
    __copyright__,
    __email__,
    __license__,
    __maintainer__,
    __repository__,
    __status__,
    __version__,
)


class TestAbout:
    """Test cases for package metadata."""

    def test_author(self) -> None:
        """Test __author__ constant."""
        assert __author__ == "GoogolGenius"
        assert isinstance(__author__, str)

    def test_repository(self) -> None:
        """Test __repository__ constant."""
        assert __repository__ == "https://github.com/GoogolGenius/RavyAPI.py"
        assert isinstance(__repository__, str)
        assert __repository__.startswith("https://github.com/")

    def test_copyright(self) -> None:
        """Test __copyright__ constant."""
        assert __copyright__ == "Copyright 2022-Present GoogolGenius"
        assert isinstance(__copyright__, str)
        assert "GoogolGenius" in __copyright__

    def test_license(self) -> None:
        """Test __license__ constant."""
        assert __license__ == "Apache v2"
        assert isinstance(__license__, str)

    def test_version(self) -> None:
        """Test __version__ constant."""
        assert __version__ == "0.1.0a"
        assert isinstance(__version__, str)

    def test_maintainer(self) -> None:
        """Test __maintainer__ constant."""
        assert __maintainer__ == "GoogolGenius"
        assert isinstance(__maintainer__, str)

    def test_email(self) -> None:
        """Test __email__ constant."""
        assert __email__ == "erich.nguyen@outlook.com"
        assert isinstance(__email__, str)
        assert "@" in __email__

    def test_status(self) -> None:
        """Test __status__ constant."""
        assert __status__ == "Development"
        assert isinstance(__status__, str)

    def test_all_exports(self) -> None:
        """Test __all__ contains all expected exports."""
        expected_exports = {
            "__author__",
            "__repository__",
            "__copyright__",
            "__license__",
            "__version__",
            "__maintainer__",
            "__email__",
            "__status__",
        }
        assert set(__all__) == expected_exports

    def test_all_is_tuple(self) -> None:
        """Test __all__ is a tuple."""
        assert isinstance(__all__, tuple)

    def test_version_format(self) -> None:
        """Test version follows semantic versioning format."""
        # Basic check for version format (major.minor.patch with optional alpha/beta)
        version_parts = __version__.split(".")
        assert len(version_parts) >= 2  # At least major.minor

        # Check that the first part is numeric
        assert version_parts[0].isdigit()
        assert version_parts[1].isdigit()

    def test_email_format(self) -> None:
        """Test email follows basic email format."""
        assert "@" in __email__
        assert "." in __email__
        parts = __email__.split("@")
        assert len(parts) == 2
        assert len(parts[0]) > 0  # Username part
        assert len(parts[1]) > 0  # Domain part

    def test_repository_format(self) -> None:
        """Test repository URL format."""
        assert __repository__.startswith("https://github.com/")
        assert __repository__.endswith("/RavyAPI.py")

        # Extract username/repo
        repo_path = __repository__.replace("https://github.com/", "")
        assert "/" in repo_path
        username, repo_name = repo_path.split("/")
        assert username == "GoogolGenius"
        assert repo_name == "RavyAPI.py"

    def test_constants_are_strings(self) -> None:
        """Test all constants are strings."""
        constants = [
            __author__,
            __repository__,
            __copyright__,
            __license__,
            __version__,
            __maintainer__,
            __email__,
            __status__,
        ]

        for constant in constants:
            assert isinstance(constant, str)
            assert len(constant) > 0  # Non-empty strings

    def test_author_and_maintainer_consistency(self) -> None:
        """Test author and maintainer are the same."""
        assert __author__ == __maintainer__
