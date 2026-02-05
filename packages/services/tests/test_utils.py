from services.utils import parse_comma_list


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
