"""Tests for FEC CSV parsing dispatcher."""

from __future__ import annotations

import pytest
from services.report.constants import SUPPORTED_FORM_TYPES
from services.report.parse import parse_fec_csv

# Sample valid F3 CSV content for testing
VALID_F3_CSV = (
    b'"HDR","FEC","8.0","Test","1.0","",""\n'
    b'"SA11AI","C00123456","TX001","","","IND","","DOE","JOHN","","","","123 MAIN ST",'
    b'"","CITY","TX","12345","P2024","","20240101","100.00","100.00","","CONTRIBUTION",'
    b'"ACME","ENGINEER","","","","","","","","","","","","","","","","",""'
)


class TestParseFecCsv:
    """Tests for parse_fec_csv function."""

    def test_parse_fec_csv_requires_form_type(self):
        """Test that parse_fec_csv raises ValueError when form_type is None."""
        with pytest.raises(ValueError, match="form_type is required"):
            parse_fec_csv(VALID_F3_CSV, form_type=None)

    def test_parse_fec_csv_requires_form_type_empty_string(self):
        """Test that parse_fec_csv raises ValueError when form_type is empty."""
        with pytest.raises(ValueError, match="form_type is required"):
            parse_fec_csv(VALID_F3_CSV, form_type="")

    def test_parse_fec_csv_rejects_unsupported_f3x(self):
        """Test that parse_fec_csv raises ValueError for F3X (unsupported)."""
        with pytest.raises(ValueError, match="Form type 'F3X' is not supported"):
            parse_fec_csv(VALID_F3_CSV, form_type="F3X")

    def test_parse_fec_csv_rejects_unsupported_f3p(self):
        """Test that parse_fec_csv raises ValueError for F3P (unsupported)."""
        with pytest.raises(ValueError, match="Form type 'F3P' is not supported"):
            parse_fec_csv(VALID_F3_CSV, form_type="F3P")

    def test_parse_fec_csv_rejects_amended_unsupported(self):
        """Test that amended unsupported forms are also rejected."""
        with pytest.raises(ValueError, match="Form type 'F3XA' is not supported"):
            parse_fec_csv(VALID_F3_CSV, form_type="F3XA")

    def test_parse_fec_csv_error_lists_supported_types(self):
        """Test that error message lists supported form types."""
        with pytest.raises(ValueError) as exc_info:
            parse_fec_csv(VALID_F3_CSV, form_type="F3X")

        error_message = str(exc_info.value)
        for supported_type in SUPPORTED_FORM_TYPES:
            assert supported_type in error_message

    def test_parse_fec_csv_accepts_f3(self):
        """Test that parse_fec_csv accepts F3 form type."""
        result = parse_fec_csv(VALID_F3_CSV, form_type="F3")
        assert result is not None
        assert result.form_type == "F3"

    def test_parse_fec_csv_accepts_amended_f3(self):
        """Test that parse_fec_csv accepts F3A (amended F3)."""
        result = parse_fec_csv(VALID_F3_CSV, form_type="F3A")
        assert result is not None
        # Base form type should be F3
        assert result.form_type == "F3"

    def test_parse_fec_csv_accepts_f3n(self):
        """Test that parse_fec_csv accepts F3N (new F3)."""
        result = parse_fec_csv(VALID_F3_CSV, form_type="F3N")
        assert result is not None
        assert result.form_type == "F3"
