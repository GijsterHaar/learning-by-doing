from hand import Hand
import pytest


def test_check_invalid_none() -> None:
    with pytest.raises(TypeError):
        assert Hand(None)

def test_check_invalid_int() -> None:
    with pytest.raises(TypeError):
        assert Hand(12)

def test_check_invalid_empty_string() -> None:
    with pytest.raises(ValueError):
        assert Hand('')

def test_check_invalid_not_enough_cards() -> None:
    with pytest.raises(ValueError):
        assert Hand('7H')

def test_check_invalid_to_manny_cards() -> None:
    with pytest.raises(ValueError):
        assert Hand('7H 8H 2H 5C 10D JD')

def test_check_invalid_wrong_rank_in_cards() -> None:
    with pytest.raises(ValueError):
        assert Hand('7H 8H 2H 1C 10D')

def test_check_invalid_wrong_suit_in_cards() -> None:
    with pytest.raises(ValueError):
        assert Hand('7L 8H 2H 2C 10D')

def test_check_invalid_valid_hand() -> None:
    assert Hand('7D 8H 2H 2C 10D')