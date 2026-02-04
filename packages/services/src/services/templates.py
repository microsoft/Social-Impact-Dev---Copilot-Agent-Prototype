"""Email templates for notification services."""

from __future__ import annotations


def build_filing_notification_html(
    filing_count: int,
    summary: str,
    files: list[dict],
    file_urls: list[str],
) -> str:
    """Build HTML email content for filing notifications."""
    files_html = ""
    if file_urls:
        files_html = "<h3>Files</h3><ul>"
        for i, url in enumerate(file_urls):
            file = files[i] if i < len(files) else {}
            name = file.get("committee_name", file.get("file_number", f"File {i + 1}"))
            files_html += f'<li><a href="{url}">{name}</a></li>'
        files_html += "</ul>"

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        h2 {{ color: #0066cc; }}
        .summary {{ background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        ul {{ padding-left: 20px; }}
        a {{ color: #0066cc; }}
    </style>
</head>
<body>
    <h2>FEC Filing Update</h2>
    <p><strong>{filing_count}</strong> new filing(s) have been processed.</p>

    <div class="summary">
        <h3>Summary</h3>
        <p>{summary}</p>
    </div>

    {files_html}

    <hr>
    <p style="font-size: 12px; color: #666;">
        This is an automated notification from the FEC Data Sync system.
    </p>
</body>
</html>"""


def build_filing_notification_plain_text(
    filing_count: int,
    summary: str,
    files: list[dict],
    file_urls: list[str],
) -> str:
    """Build plain text email content for filing notifications."""
    lines = [
        "FEC Filing Update",
        "=" * 40,
        "",
        f"{filing_count} new filing(s) have been processed.",
        "",
        "Summary:",
        "-" * 20,
        summary,
        "",
    ]

    if file_urls:
        lines.append("Files:")
        lines.append("-" * 20)
        for i, url in enumerate(file_urls):
            file = files[i] if i < len(files) else {}
            name = file.get("committee_name", file.get("file_number", f"File {i + 1}"))
            lines.append(f"- {name}: {url}")

    lines.extend(["", "-" * 40, "This is an automated notification from the FEC Data Sync system."])
    return "\n".join(lines)
