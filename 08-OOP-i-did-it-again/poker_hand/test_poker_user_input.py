from poker_user_input import User_Input
import pytest


def test_find_User_Input():
    return User_Input

def test_invali_input_None():
    with pytest.raises(TypeError):
        result = User_Input(None)

def test_invalid_input_integer():
    with pytest.raises(TypeError):
        result = User_Input(12)

def test_invalid_empty_string():
    with pytest.raises(TypeError):
        result = User_Input("")

def test_invalid_wrong_char_in_string():
    with pytest.raises(TypeError):
        result = User_Input("AS 10S 5H 7C []")

def test_invalid_not_enough_cards():
    with pytest.raises(TypeError):
        result = User_Input("AS 10S 5H 7C")

def test_invalid_to_manny_cards():
    with pytest.raises(TypeError):
        result = User_Input("AS 10S 5H 7C 8H 2C")

def test_invalid_unknown_rank():
    with pytest.raises(TypeError):
        result = User_Input("1S 10S 5H 7C 8H")

def test_invalid_unknown_suit():
    with pytest.raises(TypeError):
        result = User_Input("2Z 10S 5H 7C 8H")
    
def test_valid_input():
    result = User_Input("2H 9S 5H 7C 8H")

def test_valid_input_again():
    result = User_Input("2H 10S 5H 7C 8H")




