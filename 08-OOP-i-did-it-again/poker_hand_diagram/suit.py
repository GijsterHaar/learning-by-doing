
_VALID_SUITS = ['H', 'C', 'D', 'S']

class Suit:
    def __init__(self, suit: object):
        self.suit = suit
        self._check_invalid()

    def _check_invalid(self) -> str:
        if not isinstance(self.suit, str) or self.suit == "":
            raise TypeError("Your input is invalid")
        if not self.suit in _VALID_SUITS:
            raise ValueError("That's not a suit")
        return self.suit 


    def __eq__(self, other: object) -> bool:
        if isinstance(other, Suit):
            return self.suit == other.suit
        else:
            raise AssertionError