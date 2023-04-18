import pytest
from pure_poker import description_poker_hand

def test_empty_string():
    result = description_poker_hand('')
    assert result == "Sorry, that's invalid"

def test_no_string_integer():
    result = description_poker_hand(7)
    assert result == "Sorry, that's invalid"

def test_no_string_list():
    result = description_poker_hand([])
    assert result == "Sorry, that's invalid"

def test_no_string_bolean():
    result = description_poker_hand(True)
    assert result == "Sorry, that's invalid"

def test_one_card():
    result = description_poker_hand('5H')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_14_invalid_wrong_rank():
    result = description_poker_hand('1H 3C 4C 5C 6H')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_14_invalid_wrong_suit():
    result = description_poker_hand('7H 3C 4C 5C 6K')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_14_invalid_wrong_rank_and_suit():
    result = description_poker_hand('1H 3C 4C 5C 6K')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_15_invalid_wrong_rank():
    result = description_poker_hand('2H 3H 4C 5C 11H')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_15_invalid_wrong_suit():
    result = description_poker_hand('2H 3H 4C 5C 10K')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_15_invalid_wrong_rank_and_suit():
    result = description_poker_hand('2K 3H 4C 5C 11H')
    assert result == "Sorry, that's invalid"

def test_high_card():
    result = description_poker_hand('2H 4H 6C 8C 10H')
    assert result == 'High Card'

def test_one_pair():
    result = description_poker_hand('2H 4H 6C 10C 10H')
    assert result == 'One Pair'

def test_two_pair():
    result = description_poker_hand('6H 4H 6C 10C 10H')
    assert result == 'Two Pair'

def test_three_of_a_kind():
    result = description_poker_hand('JH 6H JC JD 10H')
    assert result == 'Three Of A Kind'

def test_four_of_a_kind():
    result = description_poker_hand('6H 6S 6C 6D 10H')
    assert result == 'Four Of A Kind'

def test_full_house():
    result = description_poker_hand('6H 6S 6C 10D 10H')
    assert result == 'Full House'

def test_straight():
    result = description_poker_hand('7H 8C 9H 10H JD')
    assert result == 'Straight'

def test_flush():
    result = description_poker_hand('2H 4H 6H 8H 10H')
    assert result == 'Flush'

def test_straight_flush():
    result = description_poker_hand('6H 7H 8H 9H 10H')
    assert result == 'Straight Flush'

def test_royal_flush():
    result = description_poker_hand('10H JH QH KH AH')
    assert result == 'Royal Flush'