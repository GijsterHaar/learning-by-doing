RANKS = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
                  '9': '9', '10': '10', 'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
SUITS = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}


class Card:
    def __init__(self, short_description):
        self.rank = RANKS[short_description[:-1]]
        self.suit = SUITS[short_description[-1]]
        self.description = f"a {RANKS[short_description[:-1]]} of {SUITS[short_description[-1]]}"
