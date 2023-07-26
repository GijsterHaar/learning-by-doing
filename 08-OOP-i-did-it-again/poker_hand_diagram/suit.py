_VALID_SUITS = ['H', 'C', 'D', 'S']


class Suit:
    def __init__(self, suit: object):
        self.suit = self._check_invalid(suit)

    def _check_invalid(self, suit: object) -> str:
        if not isinstance(suit, str) or suit == "":
            raise TypeError("Your input is invalid")
        if not suit in _VALID_SUITS:
            raise ValueError("That's not a suit")
        return suit 


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Suit):
            raise TypeError()
        return self.suit == other.suit