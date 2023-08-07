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
    compare_hand_to_wins('7H 8H 2H 5C 10D', ('High Card', 1, ))

def test_one_pair() -> None:
    compare_hand_to_wins('7H 5H 2H 5C 10D', ('One Pair', 2))

def test_two_pair() -> None:
    compare_hand_to_wins('7H 5H 10H 5C 10D', ('Two Pair', 3))

def test_three_of_a_kind() -> None:
    compare_hand_to_wins('7H 5H 5D 5C 10D', ('Three Of A Kind', 4))

def test_full_house() -> None:
    compare_hand_to_wins('7H 5H 5D 5C 7D', ('Full House', 5))

def test_four_of_a_kind() -> None:
    compare_hand_to_wins('7H 5H 5D 5C 5S', ('Four Of A Kind', 6))

def test_straight() -> None:
    compare_hand_to_wins('10H KH QC JD 9H', ('Straight', 7))

def test_flush() -> None:
    compare_hand_to_wins('10H KH 2H JH 9H', ('Flush', 8))

def test_straight_flush() -> None:
    compare_hand_to_wins('10H KH 9H JH QH', ('Straight Flush', 9))

def test_royal_flush() -> None:
    compare_hand_to_wins('10H KH AH JH QH', ('Royal Flush', 10))

def test_compare_equal_hand() -> None:
    assert Hand('10H KH 9H JH QH') == Hand('10H KH 9H JH QH')

def test_compare_unequal_hand() -> None:
    assert Hand('AH KH 9H JH QH') != Hand('10H KH 9H JH QH')

def test_equality_wrong_object_type() -> bool:
    with pytest.raises(TypeError):
        assert Hand('AH KH 9H JH QH') != Hand(None) 

def test_greater_than() -> None:
    assert Hand('AH KH 10H JH QH') > Hand('10H KH 9H JH QH')

def test_not_greater_than() -> None:
    assert not Hand('7H 5H 2H 5C 10D') > Hand('10H KH 9H JH QH')

def test_lesser_then()-> None:
    assert Hand('7H 5H 5D 5C 10D') < Hand('7H 5H 5D 5C 7D')

def test_not_lesser_than()-> None:
    assert not Hand('10H KH AH JH QH') < Hand('7H 5H 5D 5C 7D')

def test_string_method() -> bool:
    result = Hand('10H KH AH JH QH')
    assert str(result) == 'Royal Flush'

def test_string_method_again() -> bool:
    result = Hand('7H 5H 5D 5C 7D')
    assert str(result) == 'Full House'

def check_for_value_error(hand: str) -> None:
    with pytest.raises(ValueError):
        assert Hand(hand)

def check_for_type_error(hand: Any) -> None:
    with pytest.raises(TypeError):
        assert Hand(hand)

def compare_hand_to_wins(hand: object, win: tuple[str,int]) -> None:
    result = Hand(hand)
    assert result._name_the_hand() == win
