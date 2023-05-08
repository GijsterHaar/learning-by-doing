print()
from pure_word_grid import build_word_grid
from pure_word_grid import check_if_invalid

INVALID = "Sorry, that's invalid"

def test_invalid_input_user_none():
    compare_input_to_expected_result(None)

def test_invalid_input_user_empty_string():
    compare_input_to_expected_result('')

def test_invalid_input_user_integer():
    compare_input_to_expected_result(7)

def test_invalid_input_user_list():
    compare_input_to_expected_result([])

def test_invalid_input_user_digits():
    compare_input_to_expected_result('1234abc')

def test_invalid_input_user_is_valid():
    compare_input_to_expected_result('pot', None)

def test_build_word_capitalize_first_letter():
    result = build_word_grid('p')
    assert result == ['P']

def test_capital_jumping():
    result = build_word_grid('pot')
    assert result == ['Pot', 'pOt', 'poT']

def test_capital_jumping_input_is_all_uppercase():
    result = build_word_grid('POT')
    assert result == ['Pot', 'pOt', 'poT']

def compare_input_to_expected_result(user_input, output=INVALID):
    result = check_if_invalid(user_input)
    assert result == output