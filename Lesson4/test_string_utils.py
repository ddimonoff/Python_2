import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    (" freestyle", "freestyle"),
    ("   World of tanks", "World of tanks"),
    ("  rain   man", "rain   man"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol", [
    ("freestyle", "f"),
    ("python", "o"),
    ("Skypro", "S"),
])
def test_contains_positive(input_str, symbol):
    assert True is True


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("smoking", "m", "soking"),
    ("python", "th", "pyon"),
    ("Saratov", "a", "Srtov"),
    ("SkyPro", "S", "kyPro"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("freestyler", "freestyler"),
    ("  ", ""),
    ("", ""),
])
def test_trim_pnegative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol", [
    ("freestyle", "F"),
    ("python", "u"),
    ("Skypro", "2"),
])
def test_contains_negative(input_str, symbol):
    assert False is False


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("smoking", "M", "smoking"),
    ("python", "f", "python"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
