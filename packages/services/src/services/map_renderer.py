"""State-level map renderer for FEC data visualization.

Generates a static PNG tile-grid map showing donation and expenditure
percentages by US state, suitable for embedding in HTML emails.
"""

from __future__ import annotations

import io
import logging

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")  # Non-interactive backend — must be set before any other matplotlib import

from .analysis import FullAnalysisResult
from .storage import BlobStorageService

logger = logging.getLogger(__name__)

# Standard US tile grid layout: state -> (col, row), origin top-left.
# Alaska and Hawaii are repositioned to the lower-left inset area.
_STATE_TILE_GRID: dict[str, tuple[int, int]] = {
    # Row 0
    "AK": (0, 0),
    "ME": (10, 0),
    # Row 1
    "WA": (0, 1),
    "MT": (1, 1),
    "ND": (2, 1),
    "MN": (3, 1),
    "MI": (7, 1),
    "VT": (9, 1),
    "NH": (10, 1),
    # Row 2
    "OR": (0, 2),
    "ID": (1, 2),
    "WY": (2, 2),
    "SD": (3, 2),
    "WI": (4, 2),
    "NY": (8, 2),
    "MA": (9, 2),
    "RI": (10, 2),
    # Row 3
    "CA": (0, 3),
    "NV": (1, 3),
    "CO": (2, 3),
    "NE": (3, 3),
    "IA": (4, 3),
    "IL": (5, 3),
    "IN": (6, 3),
    "OH": (7, 3),
    "PA": (8, 3),
    "NJ": (9, 3),
    "CT": (10, 3),
    # Row 4
    "AZ": (1, 4),
    "UT": (2, 4),
    "KS": (3, 4),
    "MO": (4, 4),
    "KY": (5, 4),
    "WV": (6, 4),
    "VA": (7, 4),
    "MD": (8, 4),
    "DE": (9, 4),
    "DC": (10, 4),
    # Row 5
    "HI": (0, 5),
    "NM": (2, 5),
    "OK": (3, 5),
    "AR": (4, 5),
    "TN": (5, 5),
    "NC": (6, 5),
    "SC": (7, 5),
    # Row 6
    "TX": (2, 6),
    "LA": (4, 6),
    "MS": (5, 6),
    "AL": (6, 6),
    "GA": (7, 6),
    # Row 7
    "FL": (7, 7),
}

_GRID_COLS = 11  # 0-10
_GRID_ROWS = 8  # 0-7


def _compute_percentages(state_totals: dict[str, float]) -> dict[str, float]:
    """Convert raw state totals to percentages of the overall total."""
    total = sum(v for v in state_totals.values() if v > 0)
    if total <= 0:
        return {}
    return {state: (amount / total * 100) for state, amount in state_totals.items() if amount > 0}


def _draw_tile_map(
    ax: plt.Axes,
    state_pcts: dict[str, float],
    title: str,
    cmap_name: str,
) -> None:
    """Draw one tile-grid choropleth on the given axes."""
    max_pct = max(state_pcts.values(), default=0.0)
    cmap = plt.get_cmap(cmap_name)
    tile = 0.88  # Tile size (< 1.0 leaves a small gap between tiles)

    for state, (col, row) in _STATE_TILE_GRID.items():
        pct = state_pcts.get(state, 0.0)

        # Map percentage to color intensity: 0% → lightest tint, max% → darkest
        if max_pct > 0 and pct > 0:
            intensity = 0.15 + (pct / max_pct) * 0.80
        else:
            intensity = 0.08  # Near-white for states with no data

        color = cmap(intensity)

        rect = plt.Rectangle(
            (col - tile / 2, -row - tile / 2),
            tile,
            tile,
            facecolor=color,
            edgecolor="white",
            linewidth=1.2,
        )
        ax.add_patch(rect)

        # Label: white text on dark tiles, dark text on light ones
        text_color = "white" if intensity > 0.55 else "#444444"
        label = f"{state}\n{pct:.1f}%" if pct > 0 else state
        ax.text(
            col,
            -row,
            label,
            ha="center",
            va="center",
            fontsize=4.2,
            fontweight="bold",
            color=text_color,
            linespacing=1.2,
        )

    ax.set_xlim(-0.7, _GRID_COLS - 0.3)
    ax.set_ylim(-_GRID_ROWS + 0.3, 0.7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=7, fontweight="bold", pad=3, color="#222222")


def render_state_map(
    donation_state_totals: dict[str, float],
    expenditure_state_totals: dict[str, float],
    *,
    width_px: int = 600,
    dpi: int = 96,
) -> bytes:
    """Render a side-by-side US tile-grid map of donations vs expenditures by state.

    Produces a PNG suitable for embedding as an <img> tag in HTML emails.

    Args:
        donation_state_totals: State code → total donation amount (Schedule A).
        expenditure_state_totals: State code → total expenditure amount (Schedule B).
        width_px: Output image width in pixels (height is derived from aspect ratio).
        dpi: Image resolution.

    Returns:
        Raw PNG bytes.
    """
    donation_pcts = _compute_percentages(donation_state_totals)
    expenditure_pcts = _compute_percentages(expenditure_state_totals)

    width_in = width_px / dpi
    height_in = width_in * 0.52  # 2:1 side-by-side aspect ratio

    fig, (ax_left, ax_right) = plt.subplots(
        1,
        2,
        figsize=(width_in, height_in),
        dpi=dpi,
        facecolor="white",
    )

    _draw_tile_map(ax_left, donation_pcts, title="Donations by State (%)", cmap_name="Blues")
    _draw_tile_map(
        ax_right, expenditure_pcts, title="Expenditures by State (%)", cmap_name="Oranges"
    )

    plt.tight_layout(pad=0.4)

    buf = io.BytesIO()
    fig.savefig(
        buf, format="png", dpi=dpi, bbox_inches="tight", facecolor="white", edgecolor="none"
    )
    plt.close(fig)
    buf.seek(0)
    return buf.read()


_MAP_BLOB_FILENAME = "state_map.png"


def generate_state_map_blob(
    analysis: FullAnalysisResult,
    blob_service: BlobStorageService,
    base_path: str,
) -> str | None:
    """Render a state map from analysis data and upload it to blob storage.

    Extracts per-state donation and expenditure totals from the analysis result,
    renders the tile-grid map PNG, and uploads it under ``base_path``.

    Args:
        analysis: Full analysis result containing geography and expenditure data.
        blob_service: Blob storage service used for uploading.
        base_path: Blob path prefix (e.g. ``"C00718866/2024-Q1"``).

    Returns:
        The blob path of the uploaded file on success (e.g.
        ``"C00718866/2024-Q1/state_map.png"``), or ``None`` if there is no
        state-level data or the upload fails.
    """
    try:
        donation_totals: dict[str, float] = (
            analysis.geography.data.get("state_totals", {}) if analysis.geography else {}
        )
        expenditure_totals: dict[str, float] = (
            analysis.expenditure_analysis.data.get("state_totals", {})
            if analysis.expenditure_analysis
            else {}
        )

        if not donation_totals and not expenditure_totals:
            logger.info("No state-level data available, skipping map generation")
            return None

        png_bytes = render_state_map(donation_totals, expenditure_totals)
        blob_path = f"{base_path}/{_MAP_BLOB_FILENAME}"
        blob_service.upload_bytes(blob_path, png_bytes, content_type="image/png")
        logger.info(f"Uploaded state map: {blob_path}")
        return blob_path

    except Exception as e:
        logger.warning(f"Map generation failed, continuing without map: {e}")
        return None
