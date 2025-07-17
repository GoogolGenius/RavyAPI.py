"""Tests for URLs models."""

from __future__ import annotations

from ravyapi.api.models.urls import EditWebsiteRequest, GetWebsiteResponse


class TestGetWebsiteResponse:
    """Test class for GetWebsiteResponse model."""

    def test_get_website_response_initialization(self):
        """Test GetWebsiteResponse initialization."""
        data = {
            "isFraudulent": False,
            "message": "Safe website",
        }

        response = GetWebsiteResponse(data)

        assert response.data == data
        assert response.is_fraudulent is False
        assert response.message == "Safe website"

    def test_get_website_response_fraudulent(self):
        """Test GetWebsiteResponse with fraudulent website."""
        data = {
            "isFraudulent": True,
            "message": "Fraudulent website detected",
        }

        response = GetWebsiteResponse(data)

        assert response.data == data
        assert response.is_fraudulent is True
        assert response.message == "Fraudulent website detected"

    def test_get_website_response_repr(self):
        """Test GetWebsiteResponse repr."""
        data = {
            "isFraudulent": False,
            "message": "Safe website",
        }

        response = GetWebsiteResponse(data)

        repr_str = repr(response)
        assert "GetWebsiteResponse" in repr_str
        assert "is_fraudulent=False" in repr_str
        assert "message='Safe website'" in repr_str

    def test_get_website_response_data_property(self):
        """Test GetWebsiteResponse data property."""
        data = {
            "isFraudulent": True,
            "message": "Fraudulent website",
        }

        response = GetWebsiteResponse(data)

        assert response.data is data
        assert isinstance(response.data, dict)

    def test_get_website_response_is_fraudulent_property(self):
        """Test GetWebsiteResponse is_fraudulent property."""
        data = {
            "isFraudulent": True,
            "message": "Fraudulent website",
            "scan_date": "2023-01-01T00:00:00Z",
        }

        response = GetWebsiteResponse(data)

        assert response.is_fraudulent is True
        assert isinstance(response.is_fraudulent, bool)

    def test_get_website_response_message_property(self):
        """Test GetWebsiteResponse message property."""
        data = {
            "isFraudulent": False,
            "message": "Safe website with special chars: åäö",
        }

        response = GetWebsiteResponse(data)

        assert response.message == "Safe website with special chars: åäö"
        assert isinstance(response.message, str)

    def test_get_website_response_slots(self):
        """Test GetWebsiteResponse has proper slots."""
        data = {
            "isFraudulent": False,
            "message": "Safe website",
        }

        response = GetWebsiteResponse(data)

        assert hasattr(response, "__slots__")
        expected_slots = ("_data", "_is_fraudulent", "_message")
        assert response.__slots__ == expected_slots

    def test_get_website_response_immutable_data(self):
        """Test GetWebsiteResponse data is immutable reference."""
        data = {
            "isFraudulent": False,
            "message": "Safe website",
        }

        response = GetWebsiteResponse(data)
        original_data = response.data

        # Modify original data
        data["isFraudulent"] = True

        # Response data should reflect the change since it's a reference
        assert response.data["isFraudulent"] is True
        assert response.data is original_data

    def test_get_website_response_complex_data(self):
        """Test GetWebsiteResponse with complex data structure."""
        data = {
            "isFraudulent": True,
            "message": "Fraudulent website with complex unicode: 🚨🔒",
        }

        response = GetWebsiteResponse(data)

        assert response.data == data
        assert response.is_fraudulent is True
        assert response.message == "Fraudulent website with complex unicode: 🚨🔒"


class TestEditWebsiteRequest:
    """Test class for EditWebsiteRequest model."""

    def test_edit_website_request_initialization(self):
        """Test EditWebsiteRequest initialization."""
        is_fraudulent = True
        message = "Fraudulent website"

        request = EditWebsiteRequest(is_fraudulent, message)

        assert request.is_fraudulent is True
        assert request.message == "Fraudulent website"

    def test_edit_website_request_safe_website(self):
        """Test EditWebsiteRequest with safe website."""
        is_fraudulent = False
        message = "Safe website"

        request = EditWebsiteRequest(is_fraudulent, message)

        assert request.is_fraudulent is False
        assert request.message == "Safe website"

    def test_edit_website_request_repr(self):
        """Test EditWebsiteRequest repr."""
        is_fraudulent = True
        message = "Fraudulent website"

        request = EditWebsiteRequest(is_fraudulent, message)

        repr_str = repr(request)
        assert "EditWebsiteRequest" in repr_str
        assert "is_fraudulent=True" in repr_str
        assert "message='Fraudulent website'" in repr_str

    def test_edit_website_request_is_fraudulent_property(self):
        """Test EditWebsiteRequest is_fraudulent property."""
        is_fraudulent = True
        message = "Fraudulent website"

        request = EditWebsiteRequest(is_fraudulent, message)

        assert request.is_fraudulent is True
        assert isinstance(request.is_fraudulent, bool)

    def test_edit_website_request_message_property(self):
        """Test EditWebsiteRequest message property."""
        is_fraudulent = False
        message = "Safe website with special chars: åäö"

        request = EditWebsiteRequest(is_fraudulent, message)

        assert request.message == "Safe website with special chars: åäö"
        assert isinstance(request.message, str)

    def test_edit_website_request_to_json(self):
        """Test EditWebsiteRequest to_json method."""
        is_fraudulent = True
        message = "Fraudulent website"

        request = EditWebsiteRequest(is_fraudulent, message)

        json_data = request.to_json()

        expected_json = {
            "isFraudulent": True,
            "message": "Fraudulent website",
        }
        assert json_data == expected_json
        assert isinstance(json_data, dict)

    def test_edit_website_request_to_json_safe(self):
        """Test EditWebsiteRequest to_json with safe website."""
        is_fraudulent = False
        message = "Safe website"

        request = EditWebsiteRequest(is_fraudulent, message)

        json_data = request.to_json()

        expected_json = {
            "isFraudulent": False,
            "message": "Safe website",
        }
        assert json_data == expected_json

    def test_edit_website_request_slots(self):
        """Test EditWebsiteRequest has proper slots."""
        is_fraudulent = True
        message = "Fraudulent website"

        request = EditWebsiteRequest(is_fraudulent, message)

        assert hasattr(request, "__slots__")
        expected_slots = ("_is_fraudulent", "_message")
        assert request.__slots__ == expected_slots

    def test_edit_website_request_complex_message(self):
        """Test EditWebsiteRequest with complex message."""
        is_fraudulent = True
        message = "Fraudulent website with unicode: 🚨🔒 and special chars: åäö"

        request = EditWebsiteRequest(is_fraudulent, message)

        assert request.is_fraudulent is True
        assert (
            request.message
            == "Fraudulent website with unicode: 🚨🔒 and special chars: åäö"
        )

        json_data = request.to_json()
        assert json_data["isFraudulent"] is True
        assert (
            json_data["message"]
            == "Fraudulent website with unicode: 🚨🔒 and special chars: åäö"
        )
