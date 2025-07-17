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
"""Tests for API error classes."""

from __future__ import annotations

from ravyapi.api.errors import (
    AccessError,
    BadRequestError,
    ForbiddenError,
    HTTPError,
    NotFoundError,
    TooManyRequestsError,
    UnauthorizedError,
)


class TestHTTPError:
    """Test cases for the HTTPError class."""

    def test_http_error_initialization_dict(self) -> None:
        """Test HTTPError initialization with dictionary data."""
        error_data = {"error": "Something went wrong", "details": "More details"}
        error = HTTPError(500, error_data)

        assert error.status == 500
        assert error.exc_data == error_data

    def test_http_error_initialization_string(self) -> None:
        """Test HTTPError initialization with string data."""
        error_data = "Something went wrong"
        error = HTTPError(500, error_data)

        assert error.status == 500
        assert error.exc_data == error_data

    def test_http_error_str_dict(self) -> None:
        """Test HTTPError string representation with dictionary data."""
        error_data = {"error": "Something went wrong", "details": "More details"}
        error = HTTPError(500, error_data)

        expected = "(500) Something went wrong - More details"
        assert str(error) == expected

    def test_http_error_str_string(self) -> None:
        """Test HTTPError string representation with string data."""
        error_data = "Something went wrong"
        error = HTTPError(500, error_data)

        expected = "(500) Something went wrong"
        assert str(error) == expected

    def test_http_error_properties(self) -> None:
        """Test HTTPError properties."""
        error_data = {"error": "Test error"}
        error = HTTPError(404, error_data)

        assert error.status == 404
        assert error.exc_data == error_data

    def test_http_error_slots(self) -> None:
        """Test HTTPError has proper slots."""
        error = HTTPError(500, {})

        assert error.__slots__ == ("_status", "_exc_data")


class TestAccessError:
    """Test cases for the AccessError class."""

    def test_access_error_initialization(self) -> None:
        """Test AccessError initialization."""
        required_permission = "users.read"
        error = AccessError(required_permission)

        assert error.required == required_permission

    def test_access_error_str(self) -> None:
        """Test AccessError string representation."""
        required_permission = "users.read"
        error = AccessError(required_permission)

        expected = (
            'Insufficient permissions accessing path route requiring "users.read"'
        )
        assert str(error) == expected

    def test_access_error_properties(self) -> None:
        """Test AccessError properties."""
        required_permission = "avatars.check"
        error = AccessError(required_permission)

        assert error.required == required_permission

    def test_access_error_slots(self) -> None:
        """Test AccessError has proper slots."""
        error = AccessError("test")

        assert error.__slots__ == ("_required",)


class TestBadRequestError:
    """Test cases for the BadRequestError class."""

    def test_bad_request_error_initialization_dict(self) -> None:
        """Test BadRequestError initialization with dictionary data."""
        error_data = {"error": "Bad Request", "details": "Invalid parameter"}
        error = BadRequestError(error_data)

        assert error.status == 400
        assert error.exc_data == error_data

    def test_bad_request_error_initialization_string(self) -> None:
        """Test BadRequestError initialization with string data."""
        error_data = "Bad Request"
        error = BadRequestError(error_data)

        assert error.status == 400
        assert error.exc_data == error_data

    def test_bad_request_error_inherits_from_http_error(self) -> None:
        """Test that BadRequestError inherits from HTTPError."""
        error = BadRequestError("Bad Request")
        assert isinstance(error, HTTPError)

    def test_bad_request_error_slots(self) -> None:
        """Test BadRequestError has proper slots."""
        error = BadRequestError("test")

        assert error.__slots__ == ("_exc_data",)


class TestUnauthorizedError:
    """Test cases for the UnauthorizedError class."""

    def test_unauthorized_error_initialization_dict(self) -> None:
        """Test UnauthorizedError initialization with dictionary data."""
        error_data = {"error": "Unauthorized", "details": "Invalid token"}
        error = UnauthorizedError(error_data)

        assert error.status == 401
        assert error.exc_data == error_data

    def test_unauthorized_error_initialization_string(self) -> None:
        """Test UnauthorizedError initialization with string data."""
        error_data = "Unauthorized"
        error = UnauthorizedError(error_data)

        assert error.status == 401
        assert error.exc_data == error_data

    def test_unauthorized_error_inherits_from_http_error(self) -> None:
        """Test that UnauthorizedError inherits from HTTPError."""
        error = UnauthorizedError("Unauthorized")
        assert isinstance(error, HTTPError)

    def test_unauthorized_error_slots(self) -> None:
        """Test UnauthorizedError has proper slots."""
        error = UnauthorizedError("test")

        assert error.__slots__ == ("_exc_data",)


class TestForbiddenError:
    """Test cases for the ForbiddenError class."""

    def test_forbidden_error_initialization_dict(self) -> None:
        """Test ForbiddenError initialization with dictionary data."""
        error_data = {"error": "Forbidden", "details": "Access denied"}
        error = ForbiddenError(error_data)

        assert error.status == 403
        assert error.exc_data == error_data

    def test_forbidden_error_initialization_string(self) -> None:
        """Test ForbiddenError initialization with string data."""
        error_data = "Forbidden"
        error = ForbiddenError(error_data)

        assert error.status == 403
        assert error.exc_data == error_data

    def test_forbidden_error_inherits_from_http_error(self) -> None:
        """Test that ForbiddenError inherits from HTTPError."""
        error = ForbiddenError("Forbidden")
        assert isinstance(error, HTTPError)

    def test_forbidden_error_slots(self) -> None:
        """Test ForbiddenError has proper slots."""
        error = ForbiddenError("test")

        assert error.__slots__ == ("_exc_data",)


class TestNotFoundError:
    """Test cases for the NotFoundError class."""

    def test_not_found_error_initialization_dict(self) -> None:
        """Test NotFoundError initialization with dictionary data."""
        error_data = {"error": "Not Found", "details": "Resource not found"}
        error = NotFoundError(error_data)

        assert error.status == 404
        assert error.exc_data == error_data

    def test_not_found_error_initialization_string(self) -> None:
        """Test NotFoundError initialization with string data."""
        error_data = "Not Found"
        error = NotFoundError(error_data)

        assert error.status == 404
        assert error.exc_data == error_data

    def test_not_found_error_inherits_from_http_error(self) -> None:
        """Test that NotFoundError inherits from HTTPError."""
        error = NotFoundError("Not Found")
        assert isinstance(error, HTTPError)

    def test_not_found_error_slots(self) -> None:
        """Test NotFoundError has proper slots."""
        error = NotFoundError("test")

        assert error.__slots__ == ("_exc_data",)


class TestTooManyRequestsError:
    """Test cases for the TooManyRequestsError class."""

    def test_too_many_requests_error_initialization_dict(self) -> None:
        """Test TooManyRequestsError initialization with dictionary data."""
        error_data = {"error": "Too Many Requests", "details": "Rate limit exceeded"}
        error = TooManyRequestsError(error_data)

        assert error.status == 429
        assert error.exc_data == error_data

    def test_too_many_requests_error_initialization_string(self) -> None:
        """Test TooManyRequestsError initialization with string data."""
        error_data = "Too Many Requests"
        error = TooManyRequestsError(error_data)

        assert error.status == 429
        assert error.exc_data == error_data

    def test_too_many_requests_error_inherits_from_http_error(self) -> None:
        """Test that TooManyRequestsError inherits from HTTPError."""
        error = TooManyRequestsError("Too Many Requests")
        assert isinstance(error, HTTPError)

    def test_too_many_requests_error_slots(self) -> None:
        """Test TooManyRequestsError has proper slots."""
        error = TooManyRequestsError("test")

        assert error.__slots__ == ("_exc_data",)
