from pure_palindrome import check_for_invalid
from pure_palindrome import clean_user_input
from pure_palindrome import check_for_palindrome
INVALID_INPUT = 'Sorry, that is invalid input'

def test_if_input_is_invalid_None():
    compare_input_to_expected_result(None)

def test_if_input_is_invalid_empty_string():
    compare_input_to_expected_result('')

def test_if_input_is_invalid_integer():
    compare_input_to_expected_result(7)

def test_if_input_is_invalid_list():
    compare_input_to_expected_result([])

def test_if_input_clean_punctuation():
    check_clean_the_input('a:a[]', 'aa')

def test_if_input_clean_different_punctuation():
    check_clean_the_input('a,a:b"}[]c;', 'aabc')

def test_if_input_clean_different_punctuation_extended_capital():
    check_clean_the_input('A a:B "c?', "aabc")

def test_is_not_palindrome():
    compare_input_to_palindrome('pie', 'Not a palindrome')

def test_is_palindrome():
    compare_input_to_palindrome('otto', 'Yes, this is a palindrome')

def test_if_it_is_a_palindrome():
    compare_input_to_palindrome('evacaniseebeesinacave', 'Yes, this is a palindrome')


def compare_input_to_expected_result(user_input, output= INVALID_INPUT):
    result = check_for_invalid(user_input)
    assert result == output

def check_clean_the_input(user_input, cleaned_or_not):
    result = clean_user_input(user_input)
    assert result == cleaned_or_not

def compare_input_to_palindrome(user_input, palindrome_or_not):
    result = check_for_palindrome(user_input)
    assert result == palindrome_or_not