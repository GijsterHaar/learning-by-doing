from rank import Rank
from suit import Suit


class Card:
    def __init__(self, card: object) -> None:
            self.card = self._check_invalid_type(card)
            self.valid_rank = Rank(self.card[:-1]) # check if valid and get valids returned or error
            self.valid_suit = Suit(self.card[-1])

    def _check_invalid_type(self, card: object) -> str:
        if not isinstance(card, str):
            raise TypeError("Your input is invalid")
        if card == "":
            raise ValueError("That's not a card")
        return card

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.valid_rank == other.valid_rank
        else:
             raise TypeError("Your input is invalid")
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.valid_rank > other.valid_rank
        else:
            raise TypeError("Your input is invalid")
    
    def __lt__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.valid_rank < other.valid_rank
        else:
            raise TypeError("Your input is invalid")
    
