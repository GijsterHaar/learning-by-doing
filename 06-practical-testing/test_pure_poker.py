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


def test_length_poker_hand_14_invalid():
    result = description_poker_hand('2H 33 4C 5C 6D')
    assert result == "Sorry, that's invalid"

def test_length_poker_hand_15_invalid():
    result = description_poker_hand('22 3H 4C 5C 10D')
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
    result = description_poker_hand('6H 4H 6C 6D 10H')
    assert result == 'Three Of A Kind'