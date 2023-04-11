import pytest
from itertools import product, chain
from card import parse_card

@pytest.mark.parametrize('argument', [
    None,
    0,
    [],
    ['A', 'H'],
    ['A'],
    [3],
    {0: 'A', 1: 'H'},
    '21D',
    '13H',
    '4P',
    '11DD',
    '1D',
    '3HD',
    'CO',
    '01D',
    '05S',
    '4s',
    'fiveS',
    '8c',
    'ah',
    'aS',
    '-1H',
    ';*',
    ('J', 'C'),
    (x for x in 'AS'),
    '',
    '3',
    'A',
    'D'
])
def test_parse_card_requires_valid_argument(argument):
    with pytest.raises(ValueError):
        parse_card(argument)

@pytest.mark.parametrize('shorthand, expected_rank', [
    ('5H', '5'),
    ('AD', 'ace'),
    ('10S','10'),
    ('4C', '4'),
    ('JC', 'jack'),
    ('QD', 'queen'),
    ('KH', 'king'),
])
def test_parse_card_parses_rank_basics(shorthand, expected_rank):
    assert parse_card(shorthand)['rank'] == expected_rank

@pytest.mark.parametrize('shorthand, expected_description', [
    ('AS', 'an ace of spades'),
    ('2C', 'a two of clubs'),
    ('3C', 'a three of clubs'),
    ('4D', 'a four of diamonds'),
    ('5S', 'a five of spades'),
    ('6H', 'a six of hearts'),
    ('7C', 'a seven of clubs'),
    ('8D', 'an eight of diamonds'),
    ('9S', 'a nine of spades'),
    ('10H', 'a ten of hearts'),
    ('JD', 'a jack of diamonds'),
    ('QC', 'a queen of clubs'),
    ('KH', 'a king of hearts'),
])
def test_parse_card_description_basics(shorthand, expected_description):
    assert parse_card(shorthand)['description'] == expected_description

num_cards = [str(x) for x in range(2, 11)]
face_cards= 'AJQK'
ranks = list(chain(face_cards[0:1], num_cards, face_cards[1:]))
suits = 'CDHS'

rank_names = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
suit_names = ['clubs', 'diamonds', 'hearts', 'spades']
descriptive_names = ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                     'nine', 'ten', 'jack', 'queen', 'king']

rank_lookup = dict(zip(ranks, rank_names))
suit_lookup = dict(zip(suits, suit_names))
description_lookup = dict(zip(ranks, descriptive_names))

def article_for_rank(rank):
    return 'an' if rank in 'A8' else 'a'

def description_for_card(rank, suit):
    return f'{article_for_rank(rank)} {description_lookup[rank]} of {suit_lookup[suit]}'

def get_shorthand(rank, suit):
    return f'{rank}{suit}'

rank_tests = [(get_shorthand(r, s), rank_lookup[r]) for r, s in product(ranks, suits)]
@pytest.mark.parametrize('shorthand, expected_rank', rank_tests)
def test_parse_card_parses_rank(shorthand, expected_rank):
    assert parse_card(shorthand)['rank'] == expected_rank

suit_tests = [(get_shorthand(r, s), suit_lookup[s]) for r, s in product(ranks, suits)]
@pytest.mark.parametrize('shorthand, expected_suit', suit_tests)
def test_parse_card_parses_suit(shorthand, expected_suit):
    assert parse_card(shorthand)['suit'] == expected_suit

description_tests = [(get_shorthand(r, s), description_for_card(r, s)) for r, s in product(ranks,suits)]
@pytest.mark.parametrize('shorthand, expected_description', description_tests)
def test_parse_card_description_basics(shorthand, expected_description):
    assert parse_card(shorthand)['description'] == expected_description

