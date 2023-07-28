from suit import Suit
import pytest
from typing import Any

def test_invalid_input_None() -> None:
    check_for_type_error(None)

def test_invalid_input_integer() -> None:
    check_for_type_error(12)

def test_invalid_empty_string() -> None:
    check_for_type_error("")

def test_invalid_unknown_suit() -> None:
    with pytest.raises(ValueError):
        result = Suit("A")

def test_valid_suit() -> None:
    result = Suit("H")

def test_compare_equal_suit() -> None:
    assert Suit("H") == Suit("H")

def test_compare_unequal_suit() -> None:
    assert Suit("H") != Suit("S")

def test_compare_unequal_suit_wrong_object_type() -> None:
    check_for_type_error("H" == None)
    

def check_for_type_error(suit: Any) -> None:
    with pytest.raises(TypeError):
        assert Suit(suit)
