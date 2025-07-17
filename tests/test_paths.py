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
"""Tests for path routing."""

from __future__ import annotations

from ravyapi.api.paths import (
    Avatars,
    BasePath,
    Guilds,
    KSoft,
    Paths,
    Tokens,
    URLs,
    Users,
)


class TestBasePath:
    """Test cases for the BasePath class."""

    def test_base_path_initialization_empty(self) -> None:
        """Test BasePath initialization with empty string."""
        path = BasePath()
        assert path.route == ""
        assert str(path) == ""

    def test_base_path_initialization_with_path(self) -> None:
        """Test BasePath initialization with path string."""
        path = BasePath("/test/path")
        assert path.route == "/test/path"
        assert str(path) == "/test/path"

    def test_base_path_initialization_trailing_slash(self) -> None:
        """Test BasePath initialization strips trailing slash."""
        path = BasePath("/test/path/")
        assert path.route == "/test/path"
        assert str(path) == "/test/path"

    def test_base_path_truediv_string(self) -> None:
        """Test BasePath __truediv__ with string."""
        path = BasePath("/test")
        new_path = path / "subpath"

        assert isinstance(new_path, BasePath)
        assert new_path.route == "/test/subpath"
        assert str(new_path) == "/test/subpath"

    def test_base_path_truediv_int(self) -> None:
        """Test BasePath __truediv__ with integer."""
        path = BasePath("/test")
        new_path = path / 123

        assert isinstance(new_path, BasePath)
        assert new_path.route == "/test/123"
        assert str(new_path) == "/test/123"

    def test_base_path_truediv_chaining(self) -> None:
        """Test BasePath __truediv__ chaining."""
        path = BasePath("/test")
        new_path = path / "sub" / 456 / "end"

        assert isinstance(new_path, BasePath)
        assert new_path.route == "/test/sub/456/end"
        assert str(new_path) == "/test/sub/456/end"

    def test_base_path_id_property_with_numeric_id(self) -> None:
        """Test BasePath id property with numeric path component."""
        path = BasePath("/users/123456789")
        assert path.id == 123456789

    def test_base_path_id_property_with_multiple_numeric_components(self) -> None:
        """Test BasePath id property with multiple numeric components."""
        path = BasePath("/guilds/123/users/456")
        assert path.id == 456  # Should return the last numeric component

    def test_base_path_id_property_no_numeric_components(self) -> None:
        """Test BasePath id property with no numeric components."""
        path = BasePath("/users/current")
        assert path.id is None

    def test_base_path_id_property_empty_path(self) -> None:
        """Test BasePath id property with empty path."""
        path = BasePath()
        assert path.id is None

    def test_base_path_slots(self) -> None:
        """Test BasePath has proper slots."""
        path = BasePath()
        assert path.__slots__ == ("_base_path",)


class TestPaths:
    """Test cases for the Paths class."""

    def test_paths_avatars_property(self) -> None:
        """Test Paths avatars property."""
        paths = Paths()
        avatars = paths.avatars

        assert isinstance(avatars, Avatars)
        assert avatars.route == "/avatars"

    def test_paths_guilds_method(self) -> None:
        """Test Paths guilds method."""
        paths = Paths()
        guild_id = 123456789
        guilds = paths.guilds(guild_id)

        assert isinstance(guilds, Guilds)
        assert guilds.route == f"/guilds/{guild_id}"
        assert guilds.id == guild_id

    def test_paths_ksoft_property(self) -> None:
        """Test Paths ksoft property."""
        paths = Paths()
        ksoft = paths.ksoft

        assert isinstance(ksoft, KSoft)
        assert ksoft.route == "/ksoft"

    def test_paths_tokens_property(self) -> None:
        """Test Paths tokens property."""
        paths = Paths()
        tokens = paths.tokens

        assert isinstance(tokens, Tokens)
        assert tokens.route == "/tokens/@current"

    def test_paths_urls_property(self) -> None:
        """Test Paths urls property."""
        paths = Paths()
        urls = paths.urls

        assert isinstance(urls, URLs)
        assert urls.route == "/urls"

    def test_paths_users_method(self) -> None:
        """Test Paths users method."""
        paths = Paths()
        user_id = 987654321
        users = paths.users(user_id)

        assert isinstance(users, Users)
        assert users.route == f"/users/{user_id}"
        assert users.id == user_id

    def test_paths_slots(self) -> None:
        """Test Paths has proper slots."""
        paths = Paths()
        assert paths.__slots__ == ()


class TestAvatars:
    """Test cases for the Avatars class."""

    def test_avatars_initialization(self) -> None:
        """Test Avatars initialization."""
        avatars = Avatars()
        assert avatars.route == "/avatars"

    def test_avatars_inherits_from_base_path(self) -> None:
        """Test Avatars inherits from BasePath."""
        avatars = Avatars()
        assert isinstance(avatars, BasePath)

    def test_avatars_slots(self) -> None:
        """Test Avatars has proper slots."""
        avatars = Avatars()
        assert avatars.__slots__ == ()


class TestGuilds:
    """Test cases for the Guilds class."""

    def test_guilds_initialization(self) -> None:
        """Test Guilds initialization."""
        guild_id = 123456789
        guilds = Guilds(guild_id)
        assert guilds.route == f"/guilds/{guild_id}"
        assert guilds.id == guild_id

    def test_guilds_inherits_from_base_path(self) -> None:
        """Test Guilds inherits from BasePath."""
        guilds = Guilds(123456789)
        assert isinstance(guilds, BasePath)

    def test_guilds_slots(self) -> None:
        """Test Guilds has proper slots."""
        guilds = Guilds(123456789)
        assert guilds.__slots__ == ()


class TestKSoft:
    """Test cases for the KSoft class."""

    def test_ksoft_initialization(self) -> None:
        """Test KSoft initialization."""
        ksoft = KSoft()
        assert ksoft.route == "/ksoft"

    def test_ksoft_bans_method(self) -> None:
        """Test KSoft bans method."""
        ksoft = KSoft()
        user_id = 987654321
        bans_route = ksoft.bans(user_id)

        assert bans_route == f"/ksoft/bans/{user_id}"

    def test_ksoft_inherits_from_base_path(self) -> None:
        """Test KSoft inherits from BasePath."""
        ksoft = KSoft()
        assert isinstance(ksoft, BasePath)

    def test_ksoft_slots(self) -> None:
        """Test KSoft has proper slots."""
        ksoft = KSoft()
        assert ksoft.__slots__ == ()


class TestTokens:
    """Test cases for the Tokens class."""

    def test_tokens_initialization(self) -> None:
        """Test Tokens initialization."""
        tokens = Tokens()
        assert tokens.route == "/tokens/@current"

    def test_tokens_inherits_from_base_path(self) -> None:
        """Test Tokens inherits from BasePath."""
        tokens = Tokens()
        assert isinstance(tokens, BasePath)

    def test_tokens_slots(self) -> None:
        """Test Tokens has proper slots."""
        tokens = Tokens()
        assert tokens.__slots__ == ()


class TestURLs:
    """Test cases for the URLs class."""

    def test_urls_initialization(self) -> None:
        """Test URLs initialization."""
        urls = URLs()
        assert urls.route == "/urls"

    def test_urls_inherits_from_base_path(self) -> None:
        """Test URLs inherits from BasePath."""
        urls = URLs()
        assert isinstance(urls, BasePath)

    def test_urls_slots(self) -> None:
        """Test URLs has proper slots."""
        urls = URLs()
        assert urls.__slots__ == ()


class TestUsers:
    """Test cases for the Users class."""

    def test_users_initialization(self) -> None:
        """Test Users initialization."""
        user_id = 987654321
        users = Users(user_id)
        assert users.route == f"/users/{user_id}"
        assert users.id == user_id

    def test_users_pronouns_property(self) -> None:
        """Test Users pronouns property."""
        user_id = 987654321
        users = Users(user_id)
        pronouns_route = users.pronouns

        assert pronouns_route == f"/users/{user_id}/pronouns"

    def test_users_bans_property(self) -> None:
        """Test Users bans property."""
        user_id = 987654321
        users = Users(user_id)
        bans_route = users.bans

        assert bans_route == f"/users/{user_id}/bans"

    def test_users_whitelists_property(self) -> None:
        """Test Users whitelists property."""
        user_id = 987654321
        users = Users(user_id)
        whitelists_route = users.whitelists

        assert whitelists_route == f"/users/{user_id}/whitelists"

    def test_users_reputation_property(self) -> None:
        """Test Users reputation property."""
        user_id = 987654321
        users = Users(user_id)
        reputation_route = users.reputation

        assert reputation_route == f"/users/{user_id}/rep"

    def test_users_inherits_from_base_path(self) -> None:
        """Test Users inherits from BasePath."""
        users = Users(987654321)
        assert isinstance(users, BasePath)

    def test_users_slots(self) -> None:
        """Test Users has proper slots."""
        users = Users(987654321)
        assert users.__slots__ == ()
