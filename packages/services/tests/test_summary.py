from unittest.mock import MagicMock, patch

import pytest
from services import AzureOpenAISummaryService, SummaryResult


@pytest.fixture
def mock_openai_client():
    with patch("services.summary.AzureOpenAI") as mock:
        yield mock


# SummaryResult tests


def test_summary_result_success():
    result = SummaryResult(success=True, summary="Test summary")
    assert result.success is True
    assert result.summary == "Test summary"
    assert result.error is None


def test_summary_result_failure():
    result = SummaryResult(success=False, error="Something went wrong")
    assert result.success is False
    assert result.summary is None
    assert result.error == "Something went wrong"


# __init__ tests


def test_init_with_params(mock_openai_client):
    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )
    assert service.endpoint == "https://test.openai.azure.com"
    assert service.api_key == "test-key"
    assert service.deployment == "gpt-4"
    mock_openai_client.assert_called_once()


def test_init_from_env_vars(mock_openai_client, monkeypatch):
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://env.openai.azure.com")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "env-key")
    monkeypatch.setenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4-env")

    service = AzureOpenAISummaryService()
    assert service.endpoint == "https://env.openai.azure.com"
    assert service.api_key == "env-key"
    assert service.deployment == "gpt-4-env"


def test_init_with_custom_system_prompt(mock_openai_client):
    custom_prompt = "You are a custom assistant."
    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
        system_prompt=custom_prompt,
    )
    assert service.system_prompt == custom_prompt


def test_init_raises_without_endpoint():
    with pytest.raises(ValueError, match="endpoint or AZURE_OPENAI_ENDPOINT must be provided"):
        AzureOpenAISummaryService(api_key="key", deployment="gpt-4")


def test_init_raises_without_api_key():
    with pytest.raises(ValueError, match="api_key or AZURE_OPENAI_API_KEY must be provided"):
        AzureOpenAISummaryService(endpoint="https://test.com", deployment="gpt-4")


def test_init_raises_without_deployment():
    with pytest.raises(ValueError, match="deployment or AZURE_OPENAI_DEPLOYMENT must be provided"):
        AzureOpenAISummaryService(endpoint="https://test.com", api_key="key")


# generate_summary tests


def test_generate_summary_success(mock_openai_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "This is a summary of the filings."
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai_client.return_value = mock_client

    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )

    filings = [{"committee_name": "Test Committee", "form_type": "F3"}]
    result = service.generate_summary(filings)

    assert result.success is True
    assert result.summary == "This is a summary of the filings."
    mock_client.chat.completions.create.assert_called_once()


def test_generate_summary_empty_filings(mock_openai_client):
    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )

    result = service.generate_summary([])

    assert result.success is True
    assert result.summary == "No new filings to summarize."


def test_generate_summary_empty_response(mock_openai_client):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = None
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai_client.return_value = mock_client

    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )

    result = service.generate_summary([{"file_number": "123"}])

    assert result.success is False
    assert result.error == "Empty response from model"


def test_generate_summary_handles_exception(mock_openai_client):
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = Exception("API error")
    mock_openai_client.return_value = mock_client

    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )

    result = service.generate_summary([{"file_number": "123"}])

    assert result.success is False
    assert result.error is not None
    assert "API error" in result.error


# _format_filings tests


def test_format_filings(mock_openai_client):
    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )

    filings = [
        {
            "committee_name": "Test Committee",
            "form_type": "F3",
            "receipt_date": "2024-01-15",
        },
        {
            "committee_name": "Another Committee",
            "document_description": "Quarterly Report",
        },
    ]

    result = service._format_filings(filings)

    assert "1." in result
    assert "Test Committee" in result
    assert "Form: F3" in result
    assert "2024-01-15" in result
    assert "2." in result
    assert "Another Committee" in result
    assert "Quarterly Report" in result


def test_format_filings_empty_list(mock_openai_client):
    service = AzureOpenAISummaryService(
        endpoint="https://test.openai.azure.com",
        api_key="test-key",
        deployment="gpt-4",
    )

    result = service._format_filings([])
    assert result == ""
