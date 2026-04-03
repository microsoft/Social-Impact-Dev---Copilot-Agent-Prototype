"""Tests for the analysis extractors module."""

from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from services.analysis.extractors import (
    DonorSizeExtractor,
    ExpenditureExtractor,
    FundingSourceExtractor,
    GeographyExtractor,
    MaxOutDonorsExtractor,
    _format_name,
    _get_column,
    _parse_currency,
)
from services.report import F3CSV


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


class TestMaxOutDonorsExtractor:
    @pytest.fixture
    def extractor(self):
        return MaxOutDonorsExtractor(limit=3500.0)

    @pytest.fixture
    def mock_report(self):
        report = MagicMock()
        report.committee_name = "Test Committee"
        return report

    def test_extract_empty_contributions(self, extractor, mock_report):
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
        )
        result = extractor.extract(parsed, mock_report)
        assert result.stats["count"] == 0
        assert result.stats["total"] == 0

    def test_extract_max_out_donors(self, extractor, mock_report):
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

        parsed = F3CSV(
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

    def test_extract_skips_non_max_out_donors(self, extractor, mock_report):
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

        parsed = F3CSV(
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

        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[base_row, second_row],
        )

        result = extractor.extract(parsed, mock_report)

        # Should be deduplicated to 1 donor
        assert result.stats["count"] == 1

    def test_extract_calculates_percentages(self, extractor, mock_report):
        # One max out donor and one non-max out
        max_out_row = [
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
        non_max_out_row = [
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

        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[max_out_row, non_max_out_row],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["count"] == 1
        assert result.stats["total"] == 3500.0

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

        parsed = F3CSV(
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

    def test_max_out_threshold_is_3500(self, extractor, mock_report):
        """Test that the default max out threshold is $3,500."""
        assert extractor.limit == 3500.0

        # Donor just below limit should not be max out
        just_below_row = [
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
            "3499.99",
            "3499.99",
            "",
            "Company",
            "Job",
        ]
        # Donor at exactly the limit should be max out
        at_limit_row = [
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
            "3500.00",
            "3500.00",
            "",
            "Company",
            "Job",
        ]

        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[just_below_row, at_limit_row],
        )

        result = extractor.extract(parsed, mock_report)

        # Only the donor at exactly $3500 should be max out
        assert result.stats["count"] == 1
        assert result.data["donors"][0]["name"] == "Jane Smith"


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

        parsed = F3CSV(
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

        parsed = F3CSV(
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

        parsed = F3CSV(
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

        parsed = F3CSV(
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

        parsed = F3CSV(
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

        parsed = F3CSV(
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

        parsed = F3CSV(
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

    def test_negative_amounts_included_but_percentages_clamped(self, mock_report):
        """Test that refunds are included but percentages are clamped to 0."""
        extractor = GeographyExtractor()

        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("WA", "100.00"),  # In-state, positive
                self._make_contribution_row(
                    "CA", "-150.00"
                ),  # Out-of-state refund (makes out-state negative)
                self._make_contribution_row("OR", "100.00"),  # Out-of-state, positive
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Refunds are included in totals
        assert result.stats["in_state_total"] == 100.0
        assert result.stats["out_state_total"] == -50.0  # 100 + (-150)
        assert result.stats["total"] == 50.0  # 100 + (-50)

        # Percentages should be clamped to valid range (0-100%)
        assert result.stats["in_state_pct"] == 100  # Clamped from >100%
        assert result.stats["out_state_pct"] == 0  # Clamped from negative


class TestFundingSourceExtractor:
    """Tests for FundingSourceExtractor to verify funding source categorization."""

    @pytest.fixture
    def extractor(self):
        return FundingSourceExtractor()

    @pytest.fixture
    def mock_report(self):
        """Create a mock report."""
        return SimpleNamespace(committee_name="Test Committee")

    def _make_contribution_row(self, form_type: str, amount: str, name: str = "Donor") -> list[str]:
        """Create a contribution row with the given form type and amount.

        Form types:
        - SA11AI: Individual contributions
        - SA11B: Political party contributions
        - SA11C: PAC contributions
        - SA12: Transfers from affiliated committees
        - SA13: Loans received
        - SA14-SA17: Other receipts
        """
        return [
            form_type,  # 0: Form Type
            "C00123456",  # 1: Committee ID
            "TXN001",  # 2: Transaction ID
            "",  # 3
            "",  # 4
            "IND",  # 5: Entity Type
            "",  # 6: Organization Name
            name,  # 7: Last Name
            "",  # 8: First Name
            "",  # 9: Middle Name
            "",  # 10
            "",  # 11
            "",  # 12
            "",  # 13
            "Seattle",  # 14: City
            "WA",  # 15: State
            "98101",  # 16: ZIP
            "",  # 17
            "",  # 18
            "20240101",  # 19: Date
            amount,  # 20: Contribution Amount
            amount,  # 21: Aggregate
            "",  # 22
            "",  # 23
            "",  # 24
        ]

    def test_all_percentages_add_up_to_100(self, extractor, mock_report):
        """Test that all funding source percentages add up to 100%."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA11AI", "5000.00"),  # Individual
                self._make_contribution_row("SA11B", "1000.00"),  # Party
                self._make_contribution_row("SA11C", "2000.00"),  # PAC
                self._make_contribution_row("SA12", "1500.00"),  # Transfer
                self._make_contribution_row("SA13", "500.00"),  # Loan
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        total_pct = (
            result.stats["individuals_pct"]
            + result.stats["pacs_pct"]
            + result.stats["parties_pct"]
            + result.stats["transfers_pct"]
            + result.stats["loans_pct"]
        )
        assert abs(total_pct - 100.0) < 0.01

    def test_individual_contributions_correctly_identified(self, extractor, mock_report):
        """Test that SA11AI form types are categorized as individual contributions."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA11AI", "1000.00"),
                self._make_contribution_row("SA11AI", "2000.00"),
                self._make_contribution_row("SA11C", "500.00"),  # PAC for comparison
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["individuals_total"] == 3000.0
        assert result.stats["individuals_count"] == 2
        # 3000 / 3500 total = 85.71%
        assert abs(result.stats["individuals_pct"] - 85.71) < 0.1

    def test_pac_contributions_correctly_identified(self, extractor, mock_report):
        """Test that SA11C form types are categorized as PAC contributions."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA11C", "5000.00", "Some PAC"),
                self._make_contribution_row("SA11C", "3000.00", "Another PAC"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["pacs_total"] == 8000.0
        assert result.stats["pacs_count"] == 2
        assert result.stats["pacs_pct"] == 100.0

    def test_party_contributions_correctly_identified(self, extractor, mock_report):
        """Test that SA11B form types are categorized as party contributions."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA11B", "10000.00", "State Party"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["parties_total"] == 10000.0
        assert result.stats["parties_pct"] == 100.0

    def test_transfers_correctly_identified(self, extractor, mock_report):
        """Test that SA12 form types are categorized as transfers."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA12", "25000.00", "Affiliated Committee"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["transfers_total"] == 25000.0
        assert result.stats["transfers_pct"] == 100.0

    def test_loans_correctly_identified(self, extractor, mock_report):
        """Test that SA13 form types are categorized as loans."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA13", "50000.00", "Candidate"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["loans_total"] == 50000.0
        assert result.stats["loans_pct"] == 100.0

    def test_empty_contributions(self, extractor, mock_report):
        """Test that empty contributions result in zero percentages."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["individuals_pct"] == 0.0
        assert result.stats["pacs_pct"] == 0.0
        assert result.stats["parties_pct"] == 0.0
        assert result.stats["transfers_pct"] == 0.0
        assert result.stats["loans_pct"] == 0.0
        assert result.stats["total"] == 0.0

    def test_individuals_pct_represents_individual_vs_groups(self, extractor, mock_report):
        """Test that individuals_pct correctly shows individual vs group contributions.

        This is the key metric: what percentage of funding comes from individual
        contributors vs organized groups (PACs, parties, transfers).
        """
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                # Individual contributions: $6000 total
                self._make_contribution_row("SA11AI", "3000.00", "Person1"),
                self._make_contribution_row("SA11AI", "2000.00", "Person2"),
                self._make_contribution_row("SA11AI", "1000.00", "Person3"),
                # Group contributions: $4000 total
                self._make_contribution_row("SA11C", "2500.00", "Big PAC"),
                self._make_contribution_row("SA11B", "1000.00", "State Party"),
                self._make_contribution_row("SA12", "500.00", "Affiliated Cmte"),
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Total: $10,000
        assert result.stats["total"] == 10000.0

        # Individuals: $6000 / $10000 = 60%
        assert result.stats["individuals_pct"] == 60.0
        assert result.stats["individuals_total"] == 6000.0
        assert result.stats["individuals_count"] == 3

        # PACs: $2500 / $10000 = 25%
        assert result.stats["pacs_pct"] == 25.0

        # Parties: $1000 / $10000 = 10%
        assert result.stats["parties_pct"] == 10.0

        # Transfers: $500 / $10000 = 5%
        assert result.stats["transfers_pct"] == 5.0

        # All percentages should add to 100%
        total_pct = (
            result.stats["individuals_pct"]
            + result.stats["pacs_pct"]
            + result.stats["parties_pct"]
            + result.stats["transfers_pct"]
            + result.stats["loans_pct"]
        )
        assert total_pct == 100.0

    def test_other_sa_forms_categorized_as_other(self, extractor, mock_report):
        """Test that other SA form types (SA14, SA15, etc.) are categorized as other."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA14", "1000.00"),  # Offsets
                self._make_contribution_row("SA15", "500.00"),  # Other receipts
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["other_total"] == 1500.0
        # Other is tracked in data but not in stats percentage
        assert result.stats["total"] == 1500.0

    def test_negative_amounts_included_but_percentages_clamped(self, extractor, mock_report):
        """Test that refunds are included but percentages are clamped to 0."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("SA11AI", "1000.00"),  # Individual, positive
                self._make_contribution_row(
                    "SA11AI", "-1500.00"
                ),  # Individual refund (makes negative)
                self._make_contribution_row("SA11C", "1000.00"),  # PAC, positive
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Refunds are included in totals
        assert result.stats["individuals_total"] == -500.0  # 1000 + (-1500)
        assert result.stats["pacs_total"] == 1000.0
        assert result.stats["total"] == 500.0  # -500 + 1000

        # Percentages should be clamped to valid range (0-100%)
        assert result.stats["individuals_pct"] == 0  # Clamped from negative
        assert result.stats["pacs_pct"] == 100  # Clamped from >100%


class TestDonorSizeExtractor:
    """Tests for DonorSizeExtractor to verify small vs large donor categorization."""

    @pytest.fixture
    def extractor(self):
        return DonorSizeExtractor(threshold=25.0)

    @pytest.fixture
    def mock_report(self):
        """Create a mock report."""
        return SimpleNamespace(committee_name="Test Committee")

    def _make_contribution_row(self, amount: str, name: str = "Donor") -> list[str]:
        """Create an individual contribution row with the given amount."""
        return [
            "SA11AI",  # 0: Form Type (individual contribution)
            "C00123456",  # 1: Committee ID
            "TXN001",  # 2: Transaction ID
            "",  # 3
            "",  # 4
            "IND",  # 5: Entity Type
            "",  # 6: Organization Name
            name,  # 7: Last Name
            "John",  # 8: First Name
            "",  # 9: Middle Name
            "",  # 10
            "",  # 11
            "",  # 12
            "",  # 13
            "Seattle",  # 14: City
            "WA",  # 15: State
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

    def test_small_and_big_donors_categorized_correctly(self, extractor, mock_report):
        """Test that donations are categorized by the $25 threshold."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("10.00", "Small1"),  # Small
                self._make_contribution_row("25.00", "Small2"),  # Small (at threshold)
                self._make_contribution_row("50.00", "Big1"),  # Big
                self._make_contribution_row("100.00", "Big2"),  # Big
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["small_count"] == 2
        assert result.stats["small_total"] == 35.0  # 10 + 25
        assert result.stats["big_count"] == 2
        assert result.stats["big_total"] == 150.0  # 50 + 100

    def test_percentages_add_up_to_100(self, extractor, mock_report):
        """Test that small_pct + big_pct = 100%."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("20.00"),  # Small
                self._make_contribution_row("80.00"),  # Big
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["small_pct"] + result.stats["big_pct"] == 100.0
        assert result.stats["small_pct"] == 20.0  # $20 of $100
        assert result.stats["big_pct"] == 80.0  # $80 of $100

    def test_negative_amounts_included_but_percentages_clamped(self, extractor, mock_report):
        """Test that refunds are included in totals but percentages are clamped to 0.

        This prevents impossible percentages like -3.3% or 103.3%.
        """
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("100.00", "Donor1"),  # Big, positive
                self._make_contribution_row("-50.00", "Refund1"),  # Refund (negative, <= $25)
                self._make_contribution_row("20.00", "Small1"),  # Small, positive
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Refunds are included in totals
        assert result.stats["small_count"] == 2  # $20 and $-50 both <= $25
        assert result.stats["small_total"] == -30.0  # 20 + (-50)
        assert result.stats["big_count"] == 1
        assert result.stats["big_total"] == 100.0
        assert result.stats["total"] == 70.0  # -30 + 100

        # Percentages should be clamped to valid range (0-100%)
        assert result.stats["small_pct"] == 0  # Clamped from negative
        assert result.stats["big_pct"] == 100  # Clamped from >100%

    def test_zero_amounts_included(self, extractor, mock_report):
        """Test that zero-dollar contributions are included in counts."""
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("100.00"),
                self._make_contribution_row("0.00"),  # Zero contribution
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Zero amounts are included (could be placeholder records)
        assert result.stats["total_count"] == 2
        assert result.stats["total"] == 100.0

    def test_only_individual_contributions_included(self, extractor, mock_report):
        """Test that only SA11AI form types are included (individual contributions)."""
        pac_row = self._make_contribution_row("1000.00")
        pac_row[0] = "SA11C"  # PAC contribution, not individual

        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[
                self._make_contribution_row("50.00"),  # Individual
                pac_row,  # PAC - should be excluded
            ],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        # Only the individual contribution should be counted
        assert result.stats["total_count"] == 1
        assert result.stats["total"] == 50.0


class TestExpenditureExtractor:
    """Tests for ExpenditureExtractor, including per-state totals."""

    @pytest.fixture
    def extractor(self):
        return ExpenditureExtractor()

    @pytest.fixture
    def mock_report(self):
        return SimpleNamespace(committee_name="Test Committee")

    def _make_disbursement_row(
        self, amount: str, state: str = "CA", purpose: str = "CONSULTING"
    ) -> list:
        row = [""] * 30
        row[0] = "SB21B"  # Form type
        row[1] = "C00123456"  # Committee ID
        row[5] = "ORG"  # Entity type
        row[6] = "Acme Corp"  # Payee org name
        row[14] = "Los Angeles"  # City
        row[15] = state  # State
        row[19] = "20240101"  # Date
        row[20] = amount  # Amount
        row[22] = purpose  # Purpose
        return row

    def test_state_totals_populated(self, extractor, mock_report):
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[
                self._make_disbursement_row("1000.00", state="CA"),
                self._make_disbursement_row("500.00", state="CA"),
                self._make_disbursement_row("750.00", state="TX"),
            ],
        )

        result = extractor.extract(parsed, mock_report)

        assert "state_totals" in result.data
        assert result.data["state_totals"]["CA"] == pytest.approx(1500.0)
        assert result.data["state_totals"]["TX"] == pytest.approx(750.0)

    def test_state_codes_uppercased(self, extractor, mock_report):
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[self._make_disbursement_row("200.00", state="ca")],
        )

        result = extractor.extract(parsed, mock_report)

        assert "CA" in result.data["state_totals"]
        assert "ca" not in result.data["state_totals"]

    def test_empty_state_excluded_from_totals(self, extractor, mock_report):
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[self._make_disbursement_row("300.00", state="")],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.data["state_totals"] == {}

    def test_total_expenditures_correct(self, extractor, mock_report):
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[
                self._make_disbursement_row("400.00", state="NY"),
                self._make_disbursement_row("600.00", state="FL"),
            ],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.stats["total_expenditures"] == pytest.approx(1000.0)
        assert result.data["state_totals"]["NY"] == pytest.approx(400.0)
        assert result.data["state_totals"]["FL"] == pytest.approx(600.0)

    def test_empty_disbursements(self, extractor, mock_report):
        parsed = F3CSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[],
        )

        result = extractor.extract(parsed, mock_report)

        assert result.data["state_totals"] == {}
        assert result.stats["total_expenditures"] == 0.0
