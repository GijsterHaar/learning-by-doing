import pytest
from cards import parse_card

def test_parse_card_recognize_empty_string():
    with pytest.raises(ValueError, match= r'.*input.*'):
        result = parse_card('')


def test_parse_card_recognize_invalid_input_char_lower():
    with pytest.raises(ValueError, match= r'.*capital.*'):
        result = parse_card('as')


def test_parse_card_less_than_two_characters():
    with pytest.raises(ValueError, match= r'.*amount.*'):
        result = parse_card('A')


def test_parse_card_more_than_three_characters():
    with pytest.raises(ValueError, match= r'.*amount.*'):
        result = parse_card('A10C')



def test_parse_card_correct_input_with_two_char_parsed_correct():
    result = parse_card('5H')
    assert result == {
        'rank': '5',
        'suit': 'hearts',
        'description': 'a five of hearts'
    }

def test_parse_card_correct_input_with_two_char_parsed_correct_extra():
    result = parse_card('KS')
    assert result == {
        'rank': 'king',
        'suit': 'spades',
        'description': 'a king of spades'
    }

def test_parse_card_with_enter_10_parsed_correct():
    result = parse_card('10C')
    assert result == {
        'rank': '10',
        'suit': 'clubs',
        'description': 'a ten of clubs'
    }

def test_parse_card_incorrect_input_rank_two_char():
    with pytest.raises(ValueError, match= r'.*rank.*'):
        result = parse_card('1C')


def test_parse_card_incorrect_input_rank_three_char():
    with pytest.raises(ValueError, match= r'.*rank.*'):
        result = parse_card('11C')



# def test_parse_card_incorrect_input_suit_two_char
# def test_parse_card_incorrect_input_suit_two_char
# def test_parse_card_with_incorrect_input_accent
# def test_parse_card_with_incorrect_input_emoij
# def test_correct_use_of_a_or_an