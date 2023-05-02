print()
from pure_new_number import check_for_valid_input
from pure_new_number import check_guess
from pure_new_number import check_end_message

INVALID_INPUT = 'Invalid input'

def test_find_pure_number():
    assert check_for_valid_input

def test_invalid_input_empty_string():
    compare_input_to_expected_result('')

def test_invalid_input_none():
    compare_input_to_expected_result(None)

def test_invalid_input_list():
    compare_input_to_expected_result([])

def test_invalid_input_list_in_string():
    compare_input_to_expected_result('[]')

def test_invalid_input_lower_than_one():
    compare_input_to_expected_result(0)

def test_invalid_input_higher_than_hundred():
    compare_input_to_expected_result(101)

def test_valid_input():
    compare_input_to_expected_result(27, True)

def test_input_winning_guess():
    result = check_guess(8, 8)
    assert result == False

def test_input_to_low():
    result = check_guess(4, 78)
    assert result == "To low"

def test_input_to_high():
    result = check_guess(78, 45)
    assert result == "To high"

def test_get_end_message_guessed():
    result = check_end_message(50, 50)
    assert result == True

def test_get_end_message_not_guessed():
    result = check_end_message(50, 40)
    assert result == False

def compare_input_to_expected_result(data, guess=INVALID_INPUT):
    result = check_for_valid_input(data)
    assert result == guess