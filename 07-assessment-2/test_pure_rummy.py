from pure_rummy import description_rummy_hand
INVALID_STRING = 'INVALID'

def test_find_function():
    assert description_rummy_hand

def test_invalid_input_empty_string():
    compare_input_to_expected_result('')

def test_invalid_input_none():
    compare_input_to_expected_result(None)

def test_invalid_input_int():
    compare_input_to_expected_result(12)

def test_invalid_input_list():
    compare_input_to_expected_result([])

def test_invalid_input_wrong_numbers_of_cards():
    compare_input_to_expected_result("AS")

def test_three_of_a_kind_ranks():
    compare_input_to_expected_result("AC AS 5C 10C AH 2H 5H", "LOSE")

def test_three_of_a_kind_ranks_and_four_others_all_different():
    compare_input_to_expected_result("AC AS 5C 10C AH 2H 3H", "LOSE")

def test_invalid_input_with_at_least_twenty_characters_but_10_in_it_and_one_space_missing():
    compare_input_to_expected_result("10C10S 5C 10C AH 2H 5H")

def test_valid_input_ranks_with_to_manny_spaces_in_between():
    compare_input_to_expected_result("10C    10S 5C   10C AH 2H 5H", "LOSE")

def test_invalid_input_with_eight_cards():
    compare_input_to_expected_result("AC AS 5C 10C AH 2H 3H 6H")

def test_invalid_input_lower():
    compare_input_to_expected_result("ac as 5c 10c 2h 5h ah", "LOSE")

def test_four_of_a_kind_ranks():
    compare_input_to_expected_result("AC AS 5C 10S AH AD 5H", "LOSE")

def test_four_of_a_kind_ranks_and_three_others_all_different():
    compare_input_to_expected_result("AC AS 5C 10S AH AD 3H", "LOSE")

def test_three_and_four_of_a_kind_ranks():
    compare_input_to_expected_result("AC AS 10S 10C AH AD 10H", "WIN")

def test_invalid_input_with_unknown_suit():
    compare_input_to_expected_result("AC AS 5C 10B AH 2H 5H")



def compare_input_to_expected_result(user_input, rummy_hand=INVALID_STRING):
    result = description_rummy_hand(user_input)
    assert result == rummy_hand