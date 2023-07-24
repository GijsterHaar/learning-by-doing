from suit import Suit
import pytest


def test_invalid_input_None() -> None:
    with pytest.raises(TypeError):
        result = Suit(None)

def test_invalid_input_integer() -> None:
    with pytest.raises(TypeError):
        result = Suit(12)

def test_invalid_empty_string() -> None:
    with pytest.raises(TypeError):
        result = Suit("")

def test_invalid_unknown_suit() -> None:
    with pytest.raises(ValueError):
        result = Suit("A")

def test_valid_suit() -> None:
    result = Suit("H")

def test_compare_equal_suit() -> None:
    assert Suit("H") == Suit("H")

def test_compare_unequal_suit() -> None:
    assert Suit("H") != Suit("S")

def test_compare_unequal_suit_error() -> None:
    with pytest.raises(AssertionError):
        assert Suit("H") == Suit("S")
