_VALID_RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']


class Rank:
    def __init__(self, rank: object) -> None:
        self.rank = self._check_invalid(rank)

    def _check_invalid(self, rank: object) -> str:
        if not isinstance(rank, str) :
            raise TypeError("Your input is invalid")
        if not rank in _VALID_RANKS:
            raise ValueError("That's not a rank")
        return rank
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return self.rank == other.rank
        else:
            raise TypeError("Your input is invalid")
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return _VALID_RANKS.index(self.rank) > _VALID_RANKS.index(other.rank)
        else:
            raise TypeError("Your input is invalid")

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return _VALID_RANKS.index(self.rank) < _VALID_RANKS.index(other.rank)
        else:
            raise TypeError("Your input is invalid")