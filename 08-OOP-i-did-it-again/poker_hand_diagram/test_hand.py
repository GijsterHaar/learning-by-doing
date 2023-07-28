from hand import Hand
import pytest
from typing import Any


def test_check_invalid_none() -> None:
    check_for_type_error(None)

def test_check_invalid_int() -> None:
    check_for_type_error(12)

def test_check_invalid_list_of_string() -> None:
    check_for_type_error(['7H', '9C'])

def test_check_invalid_empty_string() -> None:
    check_for_value_error('')

def test_check_invalid_not_enough_cards() -> None:
    check_for_value_error('7H')

def test_check_invalid_to_manny_cards() -> None:
    check_for_value_error('7H 8H 2H 5C 10D JD')

def test_check_invalid_wrong_rank_in_cards() -> None:
    check_for_value_error('7H 8H 2H 1C 10D')

def test_check_invalid_wrong_suit_in_cards() -> None:
    check_for_value_error('7L 8H 2H 2C 10D')

def test_check_for_duplicate_cards() -> None:
    check_for_value_error('7D 8H 2C 2C 10D')

def test_check_invalid_with_valid_hand() -> None:
    assert Hand('7D 8H 2H 2C 10D')

def test_check_sorted_hand_from_check_invalid() -> None:
    result = Hand("7H 8H 2H 5C 10D")
    assert result.hand == ['10D','2H','5C','7H','8H']

def test_for_high_card() -> None:
    result = Hand('7H 8H 2H 5C 10D')
    assert result.name_the_hand() == 'High Card'

def test_one_pair() -> None:
    result =  Hand('7H 5H 2H 5C 10D')
    assert result.name_the_hand() == 'One Pair'

def test_two_pair() -> None:
    result = Hand('7H 5H 10H 5C 10D')
    assert result.name_the_hand() == 'Two Pair'

def test_three_of_a_kind() -> None:
    result = Hand('7H 5H 5D 5C 10D')
    assert result.name_the_hand() == 'Three of a Kind'

def test_full_house() -> None:
    result = Hand('7H 5H 5D 5C 7D')
    assert result.name_the_hand() == 'Full House'

def test_four_of_a_kind() -> None:
    result = Hand('7H 5H 5D 5C 5S')
    assert result.name_the_hand() == 'Four of a Kind'

def check_for_value_error(hand: str) -> None:
    with pytest.raises(ValueError):
        assert Hand(hand)

def check_for_type_error(hand: Any) -> None:
    with pytest.raises(TypeError):
        assert Hand(hand)
