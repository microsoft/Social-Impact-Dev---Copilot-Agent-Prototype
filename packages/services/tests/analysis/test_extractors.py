"""Tests for the analysis extractors module."""

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from services.analysis.extractors import (
    GeographyExtractor,
    MaxedDonorsExtractor,
    _format_name,
    _get_column,
    _parse_currency,
)
from services.report.format import ParsedQuarterlyCSV


class TestParsingHelpers:
    def test_parse_currency_valid(self):
        assert _parse_currency("1000.00") == 1000.0
        assert _parse_currency("1,234.56") == 1234.56
        assert _parse_currency('"3500.00"') == 3500.0

    def test_parse_currency_empty(self):
        assert _parse_currency("") == 0.0
        assert _parse_currency("   ") == 0.0

    def test_parse_currency_invalid(self):
        assert _parse_currency("not_a_number") == 0.0

    def test_get_column_valid(self):
        row = ["a", "b", "c"]
        assert _get_column(row, 0) == "a"
        assert _get_column(row, 2) == "c"

    def test_get_column_out_of_bounds(self):
        row = ["a", "b"]
        assert _get_column(row, 5) == ""
        assert _get_column(row, 5, "default") == "default"

    def test_format_name(self):
        assert _format_name("John", "Doe") == "John Doe"
        assert _format_name("John", "Doe", "Michael") == "John Michael Doe"
        assert _format_name("", "Doe") == "Doe"


class TestMaxedDonorsExtractor:
    @pytest.fixture
    def extractor(self):
        return MaxedDonorsExtractor(limit=3500.0)

    @pytest.fixture
    def mock_report(self):
        report = MagicMock()
        report.committee_name = "Test Committee"
        return report

    def test_extract_empty_contributions(self, extractor, mock_report):
        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
        )
        result = extractor.extract(parsed, mock_report)
        assert result.stats["count"] == 0
        assert result.stats["total"] == 0

    def test_extract_maxed_donors(self, extractor, mock_report):
        # Create a contribution row with aggregate >= 3500
        # Format matches SCHEDULE_A_COLUMNS order
        contribution_row = [
            "SA11AI",  # 0: Form Type
            "C00123456",  # 1: Committee ID
            "TXN001",  # 2: Transaction ID
            "",  # 3: Back Reference Transaction ID
            "",  # 4: Back Reference Schedule
            "IND",  # 5: Entity Type
            "",  # 6: Organization Name
            "Doe",  # 7: Last Name
            "John",  # 8: First Name
            "",  # 9: Middle Name
            "",  # 10: Prefix
            "",  # 11: Suffix
            "123 Main St",  # 12: Street 1
            "",  # 13: Street 2
            "Seattle",  # 14: City
            "WA",  # 15: State
            "98101",  # 16: ZIP
            "",  # 17: Election Code
            "",  # 18: Election Other Description
            "20240101",  # 19: Contribution Date
            "3500.00",  # 20: Contribution Amount
            "3500.00",  # 21: Contribution Aggregate
            "",  # 22: Contribution Purpose Description
            "Tech Company",  # 23: Contributor Employer
            "Engineer",  # 24: Contributor Occupation
        ]

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[contribution_row],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["count"] == 1
        assert result.stats["total"] == 3500.0
        assert len(result.data["donors"]) == 1
        assert result.data["donors"][0]["name"] == "John Doe"
        assert result.data["donors"][0]["employer"] == "Tech Company"
        assert result.data["donors"][0]["state"] == "WA"

    def test_extract_skips_non_maxed_donors(self, extractor, mock_report):
        # Contribution below limit
        contribution_row = [
            "SA11AI",
            "C00123456",
            "TXN001",
            "",
            "",
            "IND",
            "",
            "Smith",
            "Jane",
            "",
            "",
            "",
            "456 Oak Ave",
            "",
            "Portland",
            "OR",
            "97201",
            "",
            "",
            "20240101",
            "500.00",  # Amount
            "500.00",  # Aggregate - below limit
            "",
            "Other Company",
            "Manager",
        ]

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[contribution_row],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["count"] == 0
        assert result.stats["total"] == 0

    def test_extract_deduplicates_donors(self, extractor, mock_report):
        # Same donor appearing twice
        base_row = [
            "SA11AI",
            "C00123456",
            "",
            "",
            "",
            "IND",
            "",
            "Doe",
            "John",
            "",
            "",
            "",
            "123 Main St",
            "",
            "Seattle",
            "WA",
            "98101",
            "",
            "",
            "20240101",
            "1750.00",
            "3500.00",
            "",
            "Tech Company",
            "Engineer",
        ]

        # Second contribution from same donor
        second_row = base_row.copy()
        second_row[2] = "TXN002"

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[base_row, second_row],
        )

        result = extractor.extract(parsed, mock_report)

        # Should be deduplicated to 1 donor
        assert result.stats["count"] == 1

    def test_extract_calculates_percentages(self, extractor, mock_report):
        # One maxed donor and one non-maxed
        maxed_row = [
            "SA11AI",
            "C00123456",
            "TXN001",
            "",
            "",
            "IND",
            "",
            "Doe",
            "John",
            "",
            "",
            "",
            "",
            "",
            "Seattle",
            "WA",
            "",
            "",
            "",
            "20240101",
            "3500.00",
            "3500.00",
            "",
            "Tech Company",
            "Engineer",
        ]
        non_maxed_row = [
            "SA11AI",
            "C00123456",
            "TXN002",
            "",
            "",
            "IND",
            "",
            "Smith",
            "Jane",
            "",
            "",
            "",
            "",
            "",
            "Portland",
            "OR",
            "",
            "",
            "",
            "20240101",
            "1500.00",
            "1500.00",
            "",
            "Other Company",
            "Manager",
        ]

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[maxed_row, non_maxed_row],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["count"] == 1
        assert result.stats["total"] == 3500.0
        assert result.stats["total_individual_contributions"] == 5000.0
        assert result.stats["pct_of_individual"] == 70.0

    def test_extract_groups_by_employer(self, extractor, mock_report):
        # Multiple donors from same employer
        def make_row(last, first, employer):
            return [
                "SA11AI",
                "C00123456",
                f"TXN_{first}",
                "",
                "",
                "IND",
                "",
                last,
                first,
                "",
                "",
                "",
                "",
                "",
                "Seattle",
                "WA",
                "",
                "",
                "",
                "20240101",
                "3500.00",
                "3500.00",
                "",
                employer,
                "Employee",
            ]

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                make_row("Doe", "John", "Tech Company"),
                make_row("Smith", "Jane", "Tech Company"),
                make_row("Jones", "Bob", "Other Corp"),
            ],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["count"] == 3
        top_employers = dict(result.data["top_employers"])
        assert top_employers["Tech Company"] == 2
        assert top_employers["Other Corp"] == 1


class TestGeographyExtractor:
    """Tests for GeographyExtractor to ensure in-state/out-of-state percentages are correct."""

    @pytest.fixture
    def mock_report(self):
        """Create a mock report with state set to WA."""
        return SimpleNamespace(
            committee_name="Test Committee",
            state="WA",
        )

    def _make_contribution_row(self, state: str, amount: str) -> list[str]:
        """Create a contribution row with the given state and amount."""
        return [
            "SA11AI",  # 0: Form Type
            "C00123456",  # 1: Committee ID
            "TXN001",  # 2: Transaction ID
            "",  # 3
            "",  # 4
            "IND",  # 5: Entity Type
            "",  # 6: Organization Name
            "Doe",  # 7: Last Name
            "John",  # 8: First Name
            "",  # 9: Middle Name
            "",  # 10
            "",  # 11
            "123 Main St",  # 12
            "",  # 13
            "Seattle",  # 14: City
            state,  # 15: State
            "98101",  # 16: ZIP
            "",  # 17
            "",  # 18
            "20240101",  # 19: Date
            amount,  # 20: Contribution Amount
            amount,  # 21: Aggregate
            "",  # 22
            "Employer",  # 23
            "Occupation",  # 24
        ]

    def test_percentages_add_up_to_100_mixed_states(self, mock_report):
        """Test that in-state + out-of-state percentages equal 100% with mixed contributions."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("WA", "1000.00"),  # In-state
                self._make_contribution_row("CA", "500.00"),  # Out-of-state
                self._make_contribution_row("WA", "500.00"),  # In-state
                self._make_contribution_row("OR", "1000.00"),  # Out-of-state
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        in_state_pct = result.stats["in_state_pct"]
        out_state_pct = result.stats["out_state_pct"]

        assert in_state_pct + out_state_pct == 100.0
        assert in_state_pct == 50.0  # $1500 of $3000
        assert out_state_pct == 50.0  # $1500 of $3000

    def test_percentages_add_up_to_100_all_in_state(self, mock_report):
        """Test percentages when all contributions are in-state."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("WA", "1000.00"),
                self._make_contribution_row("WA", "2000.00"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["in_state_pct"] + result.stats["out_state_pct"] == 100.0
        assert result.stats["in_state_pct"] == 100.0
        assert result.stats["out_state_pct"] == 0.0

    def test_percentages_add_up_to_100_all_out_of_state(self, mock_report):
        """Test percentages when all contributions are out-of-state."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("CA", "1000.00"),
                self._make_contribution_row("OR", "2000.00"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["in_state_pct"] + result.stats["out_state_pct"] == 100.0
        assert result.stats["in_state_pct"] == 0.0
        assert result.stats["out_state_pct"] == 100.0

    def test_percentages_are_zero_with_no_contributions(self, mock_report):
        """Test that percentages are 0 when there are no contributions."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["in_state_pct"] == 0.0
        assert result.stats["out_state_pct"] == 0.0
        assert result.stats["total"] == 0.0

    def test_percentages_with_decimal_amounts(self, mock_report):
        """Test that percentages add up to 100% with decimal amounts."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("WA", "333.33"),
                self._make_contribution_row("CA", "666.67"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        total_pct = result.stats["in_state_pct"] + result.stats["out_state_pct"]
        assert abs(total_pct - 100.0) < 0.01  # Allow small floating point error

    def test_unknown_state_not_included_in_percentages(self, mock_report):
        """Test that contributions with empty state are tracked separately."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("WA", "1000.00"),
                self._make_contribution_row("CA", "1000.00"),
                self._make_contribution_row("", "500.00"),  # Unknown state
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Percentages should still add to 100% (unknown excluded from calculation)
        assert result.stats["in_state_pct"] + result.stats["out_state_pct"] == 100.0
        assert result.stats["in_state_pct"] == 50.0
        assert result.stats["out_state_pct"] == 50.0
        assert result.stats["unknown_state_total"] == 500.0

    def test_case_insensitive_state_matching(self, mock_report):
        """Test that state matching is case-insensitive."""
        extractor = GeographyExtractor()

        parsed = ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("wa", "1000.00"),  # lowercase
                self._make_contribution_row("Wa", "1000.00"),  # mixed case
                self._make_contribution_row("CA", "2000.00"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["in_state_pct"] + result.stats["out_state_pct"] == 100.0
        assert result.stats["in_state_pct"] == 50.0  # $2000 of $4000
        assert result.stats["out_state_pct"] == 50.0
