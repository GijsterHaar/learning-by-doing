 
from rank import Rank
from suit import Suit


class Card:
    def __init__(self, card: object) -> None:
            self.card = self._check_invalid_type(card)
            self._get_rank_and_suit()

    def _check_invalid_type(self, card: object) -> str:
        if not isinstance(card, str):
            raise TypeError()
        if card == "":
            raise ValueError()
        return card

    def _get_rank_and_suit(self) -> None:
        if isinstance(self.card, str):
            self.valid_rank = Rank(self.card[:-1])
            self.valid_suit = Suit(self.card[-1])

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.valid_rank == other.valid_rank
        else:
             raise TypeError()
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.valid_rank > other.valid_rank
        else:
            raise TypeError()
    
    def __lt__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.valid_rank < other.valid_rank
        else:
            raise TypeError()
    
    