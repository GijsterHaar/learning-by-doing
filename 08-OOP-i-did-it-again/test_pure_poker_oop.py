from pure_poker_oop import User_Input, Hand
INVALID = "Sorry, that's invalid input"


def test_find_User_Input():
    result = User_Input

def test_invalid_input_None():
    result = User_Input(None)
    assert result.check_invalid() == INVALID

def test_invalid_input_empty_string():
    result = User_Input("")
    assert result.check_invalid() == INVALID

def test_invalid_int():
    result = User_Input(12)
    assert result.check_invalid() == INVALID

def test_invalid_char_in_string_input():
    result = User_Input("AS 10S 5H 7C []")
    assert result.check_invalid() == INVALID

def test_not_enough_cards():
    result = User_Input("AS")
    assert result.check_invalid() == INVALID

def test_to_manny_cards():
    result = User_Input("AS 10S 5H 7C 6S 9C")
    assert result.check_invalid() == INVALID

def test_split_user_input():
    result = User_Input("AS 10S 5H 7C 6S")
    assert result.split_input() == ["AS", "10S", "5H", "7C", "6S"]

def test_find_Hand():
    result = Hand

def test_count_ranks():
    result = Hand("AS 10S 10H AC 6S")
    assert result.count_ranks() == {"A": 2, "10": 2, "6": 1}

def test_count_suits():
    result = Hand("AS 10S 10H AC 6H")
    assert result.count_suits() == {"S": 2, "H": 2, "C": 1}