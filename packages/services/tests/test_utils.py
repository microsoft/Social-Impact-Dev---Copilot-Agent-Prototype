from services.utils import parse_comma_list, round_percentages


def test_parse_comma_list_basic():
    assert parse_comma_list("a,b,c") == ["a", "b", "c"]


def test_parse_comma_list_strips_whitespace():
    assert parse_comma_list("  a , b , c  ") == ["a", "b", "c"]


def test_parse_comma_list_filters_empty():
    assert parse_comma_list("a,,b,  ,c") == ["a", "b", "c"]


def test_parse_comma_list_empty_string():
    assert parse_comma_list("") == []


def test_parse_comma_list_none():
    assert parse_comma_list(None) == []


def test_parse_comma_list_whitespace_only():
    assert parse_comma_list("   ") == []


def test_parse_comma_list_single_value():
    assert parse_comma_list("single") == ["single"]


# round_percentages tests


def test_round_percentages_sums_to_100():
    """Test that rounded percentages sum to exactly 100%."""
    # This case would sum to 99.9% without the fix
    result = round_percentages({"a": 13.04, "b": 0.32, "c": 86.64})
    assert sum(result.values()) == 100.0


def test_round_percentages_preserves_simple_values():
    """Test that clean percentages are preserved."""
    result = round_percentages({"a": 50.0, "b": 50.0})
    assert result == {"a": 50.0, "b": 50.0}


def test_round_percentages_handles_empty():
    """Test empty input."""
    assert round_percentages({}) == {}


def test_round_percentages_handles_all_zeros():
    """Test all zero values."""
    result = round_percentages({"a": 0, "b": 0})
    assert result == {"a": 0.0, "b": 0.0}


def test_round_percentages_clamps_negative():
    """Test that negative values are clamped to 0."""
    result = round_percentages({"a": -50.0, "b": 150.0})
    assert result["a"] == 0.0
    assert result["b"] == 100.0


def test_round_percentages_clamps_over_100():
    """Test that values over 100 are clamped."""
    result = round_percentages({"a": 200.0, "b": -100.0})
    assert result["a"] == 100.0
    assert result["b"] == 0.0
