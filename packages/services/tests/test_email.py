from unittest.mock import MagicMock, patch

import pytest
from services import AzureEmailService, EmailMessage


@pytest.fixture
def mock_email_client():
    with patch("services.email.EmailClient") as mock:
        yield mock


@pytest.fixture
def mock_default_credential():
    with patch("services.email.DefaultAzureCredential") as mock:
        yield mock


# __init__ tests


def test_init_with_connection_string(mock_email_client):
    service = AzureEmailService(
        connection_string="endpoint=https://test.communication.azure.com",
        sender_address="sender@example.com",
    )
    mock_email_client.from_connection_string.assert_called_once_with(
        "endpoint=https://test.communication.azure.com"
    )
    assert service.sender_address == "sender@example.com"


def test_init_with_endpoint(mock_email_client, mock_default_credential):
    _service = AzureEmailService(
        endpoint="https://test.communication.azure.com",
        sender_address="sender@example.com",
    )
    mock_default_credential.assert_called_once()
    mock_email_client.assert_called_once_with(
        "https://test.communication.azure.com",
        mock_default_credential.return_value,
    )


def test_init_from_env_vars(mock_email_client, monkeypatch):
    monkeypatch.setenv("EMAIL_CONNECTION_STRING", "endpoint=https://env.azure.com")
    monkeypatch.setenv("EMAIL_SENDER_ADDRESS", "env@example.com")

    service = AzureEmailService()
    assert service.sender_address == "env@example.com"
    mock_email_client.from_connection_string.assert_called_once()


def test_init_raises_without_sender_address(mock_email_client):
    with pytest.raises(ValueError, match="sender_address or EMAIL_SENDER_ADDRESS must be provided"):
        AzureEmailService(connection_string="endpoint=https://test.azure.com")


def test_init_raises_without_connection_string_or_endpoint():
    with pytest.raises(ValueError, match="Either connection_string or endpoint must be provided"):
        AzureEmailService(sender_address="sender@example.com")


# send_email tests


def test_send_email_success(mock_email_client):
    mock_client = MagicMock()
    mock_poller = MagicMock()
    mock_poller.result.return_value = {"id": "message-123"}
    mock_client.begin_send.return_value = mock_poller
    mock_email_client.from_connection_string.return_value = mock_client

    service = AzureEmailService(
        connection_string="endpoint=https://test.azure.com",
        sender_address="sender@example.com",
    )

    message = EmailMessage(
        subject="Test Subject",
        html_content="<p>Hello</p>",
        plain_text_content="Hello",
    )
    result = service.send_email(["recipient@example.com"], message)

    assert result.success is True
    assert result.message_id == "message-123"
    mock_client.begin_send.assert_called_once()


def test_send_email_with_no_recipients(mock_email_client):
    service = AzureEmailService(
        connection_string="endpoint=https://test.azure.com",
        sender_address="sender@example.com",
    )

    message = EmailMessage(subject="Test", html_content="<p>Hello</p>")
    result = service.send_email([], message)

    assert result.success is False
    assert result.error == "No recipients provided"


def test_send_email_handles_exception(mock_email_client):
    mock_client = MagicMock()
    mock_client.begin_send.side_effect = Exception("Connection failed")
    mock_email_client.from_connection_string.return_value = mock_client

    service = AzureEmailService(
        connection_string="endpoint=https://test.azure.com",
        sender_address="sender@example.com",
    )

    message = EmailMessage(subject="Test", html_content="<p>Hello</p>")
    result = service.send_email(["recipient@example.com"], message)

    assert result.success is False
    assert result.error is not None
    assert "Connection failed" in result.error
