"""Tests for the map_renderer module."""

from unittest.mock import MagicMock

import pytest
from services.analysis.analyzers import AnalysisResult
from services.analysis.service import FullAnalysisResult
from services.map_renderer import (
    _MAP_BLOB_FILENAME,
    _STATE_TILE_GRID,
    _compute_percentages,
    generate_state_map_blob,
    render_state_map,
)


class TestComputePercentages:
    def test_basic_conversion(self):
        result = _compute_percentages({"CA": 500.0, "TX": 250.0, "NY": 250.0})
        assert result["CA"] == pytest.approx(50.0)
        assert result["TX"] == pytest.approx(25.0)
        assert result["NY"] == pytest.approx(25.0)

    def test_empty_input(self):
        assert _compute_percentages({}) == {}

    def test_all_zeros(self):
        assert _compute_percentages({"CA": 0.0, "TX": 0.0}) == {}

    def test_single_state(self):
        result = _compute_percentages({"CA": 1000.0})
        assert result["CA"] == pytest.approx(100.0)

    def test_negative_values_excluded(self):
        result = _compute_percentages({"CA": 100.0, "TX": -50.0})
        assert "TX" not in result
        assert result["CA"] == pytest.approx(100.0)

    def test_percentages_sum_to_100(self):
        totals = {"CA": 100.0, "TX": 200.0, "NY": 300.0, "FL": 400.0}
        result = _compute_percentages(totals)
        assert sum(result.values()) == pytest.approx(100.0)


class TestStateTileGrid:
    def test_all_50_states_plus_dc_present(self):
        us_states = {
            "AL",
            "AK",
            "AZ",
            "AR",
            "CA",
            "CO",
            "CT",
            "DE",
            "FL",
            "GA",
            "HI",
            "ID",
            "IL",
            "IN",
            "IA",
            "KS",
            "KY",
            "LA",
            "ME",
            "MD",
            "MA",
            "MI",
            "MN",
            "MS",
            "MO",
            "MT",
            "NE",
            "NV",
            "NH",
            "NJ",
            "NM",
            "NY",
            "NC",
            "ND",
            "OH",
            "OK",
            "OR",
            "PA",
            "RI",
            "SC",
            "SD",
            "TN",
            "TX",
            "UT",
            "VT",
            "VA",
            "WA",
            "WV",
            "WI",
            "WY",
            "DC",
        }
        assert us_states == set(_STATE_TILE_GRID.keys())

    def test_no_duplicate_positions(self):
        positions = list(_STATE_TILE_GRID.values())
        assert len(positions) == len(set(positions)), "Two states share the same tile position"


class TestRenderStateMap:
    def test_returns_png_bytes(self):
        png = render_state_map({"CA": 1000.0, "TX": 500.0}, {"CA": 200.0, "NY": 800.0})
        assert isinstance(png, bytes)
        assert png[:8] == b"\x89PNG\r\n\x1a\n"  # PNG magic bytes

    def test_empty_data_still_renders(self):
        png = render_state_map({}, {})
        assert isinstance(png, bytes)
        assert len(png) > 0

    def test_custom_width(self):
        narrow = render_state_map({"CA": 100.0}, {"TX": 100.0}, width_px=300)
        wide = render_state_map({"CA": 100.0}, {"TX": 100.0}, width_px=600)
        # Wider image should produce a larger file
        assert len(wide) > len(narrow)


class TestGenerateStateMapBlob:
    def _make_analysis(self, donation_totals=None, expenditure_totals=None):
        geo = AnalysisResult(
            feature="geography",
            data={"state_totals": donation_totals or {}},
            stats={},
            narrative="",
        )
        exp = AnalysisResult(
            feature="expenditure_analysis",
            data={
                "state_totals": expenditure_totals or {},
                "categories": {},
                "flagged_expenditures": [],
                "keywords_used": [],
            },
            stats={},
            narrative="",
        )
        return FullAnalysisResult(geography=geo, expenditure_analysis=exp)

    def test_uploads_and_returns_blob_path(self):
        blob_service = MagicMock()
        analysis = self._make_analysis({"CA": 1000.0}, {"TX": 500.0})

        result = generate_state_map_blob(analysis, blob_service, "C001/2024-Q1")

        assert result == "C001/2024-Q1/state_map.png"
        blob_service.upload_bytes.assert_called_once()
        call_args = blob_service.upload_bytes.call_args
        assert call_args[0][0] == "C001/2024-Q1/state_map.png"
        assert call_args.kwargs["content_type"] == "image/png"
        # Uploaded bytes should be valid PNG
        png_bytes = call_args[0][1]
        assert png_bytes[:8] == b"\x89PNG\r\n\x1a\n"

    def test_returns_none_when_no_state_data(self):
        blob_service = MagicMock()
        analysis = self._make_analysis({}, {})

        result = generate_state_map_blob(analysis, blob_service, "C001/2024-Q1")

        assert result is None
        blob_service.upload_bytes.assert_not_called()

    def test_returns_none_when_analysis_missing_geography(self):
        blob_service = MagicMock()
        analysis = FullAnalysisResult()

        result = generate_state_map_blob(analysis, blob_service, "C001/2024-Q1")

        assert result is None

    def test_returns_none_on_upload_failure(self):
        blob_service = MagicMock()
        blob_service.upload_bytes.side_effect = RuntimeError("network error")
        analysis = self._make_analysis({"CA": 1000.0}, {"TX": 500.0})

        result = generate_state_map_blob(analysis, blob_service, "C001/2024-Q1")

        assert result is None

    def test_blob_filename_constant_used(self):
        blob_service = MagicMock()
        analysis = self._make_analysis({"CA": 500.0}, {})

        result = generate_state_map_blob(analysis, blob_service, "C001/2024-Q1")

        assert result is not None
        assert result.endswith(_MAP_BLOB_FILENAME)
