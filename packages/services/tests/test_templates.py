from services.templates import (
    build_filing_notification_html,
    build_filing_notification_plain_text,
)

# build_filing_notification_html tests


def test_html_includes_filing_count():
    result = build_filing_notification_html(
        filing_count=5,
        summary="Test summary",
        files=[],
        file_urls=[],
    )
    assert "<strong>5</strong>" in result
    assert "new filing(s) have been processed" in result


def test_html_includes_summary():
    result = build_filing_notification_html(
        filing_count=1,
        summary="This is the summary text.",
        files=[],
        file_urls=[],
    )
    assert "This is the summary text." in result
    assert '<div class="summary">' in result


def test_html_includes_file_links():
    files = [
        {"committee_name": "Test Committee"},
        {"file_number": "12345"},
    ]
    file_urls = [
        "https://storage.blob.core.windows.net/container/file1",
        "https://storage.blob.core.windows.net/container/file2",
    ]

    result = build_filing_notification_html(
        filing_count=2,
        summary="Summary",
        files=files,
        file_urls=file_urls,
    )

    assert "<h3>Files</h3>" in result
    assert "Test Committee" in result
    assert "12345" in result
    assert file_urls[0] in result
    assert file_urls[1] in result


def test_html_no_files_section_when_empty():
    result = build_filing_notification_html(
        filing_count=1,
        summary="Summary",
        files=[],
        file_urls=[],
    )
    assert "<h3>Files</h3>" not in result


def test_html_handles_more_urls_than_files():
    files = [{"committee_name": "Only File"}]
    file_urls = [
        "https://example.com/1",
        "https://example.com/2",
    ]

    result = build_filing_notification_html(
        filing_count=2,
        summary="Summary",
        files=files,
        file_urls=file_urls,
    )

    assert "Only File" in result
    assert "File 2" in result  # Fallback name for second URL


def test_html_is_valid_structure():
    result = build_filing_notification_html(
        filing_count=1,
        summary="Test",
        files=[],
        file_urls=[],
    )
    assert result.startswith("<!DOCTYPE html>")
    assert "<html>" in result
    assert "</html>" in result
    assert "<head>" in result
    assert "<body>" in result


# build_filing_notification_plain_text tests


def test_plain_text_includes_filing_count():
    result = build_filing_notification_plain_text(
        filing_count=3,
        summary="Test summary",
        files=[],
        file_urls=[],
    )
    assert "3 new filing(s) have been processed" in result


def test_plain_text_includes_summary():
    result = build_filing_notification_plain_text(
        filing_count=1,
        summary="This is the summary.",
        files=[],
        file_urls=[],
    )
    assert "Summary:" in result
    assert "This is the summary." in result


def test_plain_text_includes_file_links():
    files = [
        {"committee_name": "Committee A"},
        {"file_number": "67890"},
    ]
    file_urls = [
        "https://example.com/file1",
        "https://example.com/file2",
    ]

    result = build_filing_notification_plain_text(
        filing_count=2,
        summary="Summary",
        files=files,
        file_urls=file_urls,
    )

    assert "Files:" in result
    assert "Committee A" in result
    assert "67890" in result
    assert "https://example.com/file1" in result
    assert "https://example.com/file2" in result


def test_plain_text_no_files_section_when_empty():
    result = build_filing_notification_plain_text(
        filing_count=1,
        summary="Summary",
        files=[],
        file_urls=[],
    )
    assert "Files:" not in result


def test_plain_text_handles_more_urls_than_files():
    files = [{"committee_name": "Single File"}]
    file_urls = [
        "https://example.com/1",
        "https://example.com/2",
    ]

    result = build_filing_notification_plain_text(
        filing_count=2,
        summary="Summary",
        files=files,
        file_urls=file_urls,
    )

    assert "Single File" in result
    assert "File 2" in result


def test_plain_text_includes_footer():
    result = build_filing_notification_plain_text(
        filing_count=1,
        summary="Test",
        files=[],
        file_urls=[],
    )
    assert "automated notification from the FEC Data Sync system" in result


def test_plain_text_has_proper_formatting():
    result = build_filing_notification_plain_text(
        filing_count=1,
        summary="Test",
        files=[],
        file_urls=[],
    )
    assert "FEC Filing Update" in result
    assert "=" * 40 in result
    assert "-" * 20 in result
