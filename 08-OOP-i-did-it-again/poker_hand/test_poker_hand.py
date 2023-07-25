from poker_hand import Hand
import pytest

def test_find_Hand():
    return Hand

def test_create_hand_wrong_rank():
    with pytest.raises(TypeError):
        result = Hand("1S 10S 5H 7C 8H")

def test_create_hand_wrong_suit():
    with pytest.raises(TypeError):
        result = Hand("2Z 10S 5H 7C 8H")

def test_valid_hand():
    result = Hand("2H 10S 5H 7C 8H")
    assert result.valid_input.input == ["2H", "10S", "5H", "7C", "8H"]

def test_high_card():
    result = Hand("7S 10S KH 9C 8H")
    assert result._check_hand() == "High card"

def test_one_pair():
    result = Hand("7S 10S KH 10C 8H")
    assert result._check_hand() == "One pair"

def test_two_pair():
    result = Hand("7S 10S 8H 10C 7H")
    assert result._check_hand() == "Two pair"

def test_three_of_a_kind():
    result = Hand("7S 10S 8H 10C 10H")
    assert result._check_hand() == "Three of a kind"

def test_full_house():
    result = Hand("8S 10S 8H 10C 10H")
    assert result._check_hand() == "Full house"

def test_four_of_a_kind():
    result = Hand("8S 10S 10H 10C 10D")
    assert result._check_hand() == "Four of a kind"

def test_royal_flush():
    result = Hand("10H JH QH KH AH")
    assert result._check_hand() == "Royal flush"






# def test_create_hand_other_hand():
#     input = User_Input("2S 10S 5H 7C 8H")
#     result = Other_Hand(input)