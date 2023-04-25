from pure_poker_steve import description_poker_hand

INVALID_STRING = 'Invalid Input'

def test_find_function():
    assert description_poker_hand

def test_invalid_input_empty_string():
    compare_input_to_expected_result('')

def test_invalid_input_none():
    compare_input_to_expected_result(None)

def test_invalid_input_int():
    compare_input_to_expected_result(12)

def test_invalid_input_list():
    compare_input_to_expected_result([])

def test_wrong_number_of_cards():
    compare_input_to_expected_result("AS")

def test_valid():
    compare_input_to_expected_result("AS 3C 5H 7D 8D", 'High Card')

def test_one_pair():
    compare_input_to_expected_result('7S 10H 7D 2C 4D', 'One Pair')

def test_two_pair():
    compare_input_to_expected_result('7S 10S JD 10H 7D' ,'Two Pair')

def test_three_of_a_kind():
    compare_input_to_expected_result('8S JH 8D KH 8C', 'Three Of A Kind')

def test_full_house():
    compare_input_to_expected_result('8S 9S 8H 9H 8C', 'Full House')

def test_four_of_a_kind():
    compare_input_to_expected_result('9S 10S 9C 9H 9D', 'Four Of A Kind')

def test_straight():
    compare_input_to_expected_result('8S 9C 7H 6S 5H', 'Straight')

def test_straight_with_ten():
    compare_input_to_expected_result('8S 9C 7H 6S 10H', 'Straight')

def test_straight_flush():
    compare_input_to_expected_result('8H 10H QH JH 9H', 'Straight Flush')

def test_royal_flush():
    compare_input_to_expected_result('10H AH QH JH KH', 'Royal Flush')

def test_flush():
    compare_input_to_expected_result('10H 5H JH 2H AH', 'Flush')

def compare_input_to_expected_result(data, poker_hand=INVALID_STRING):
    result = description_poker_hand(data)
    assert result == poker_hand
