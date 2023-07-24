
_VALID_RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class Rank:
    def __init__(self, rank: object) -> None:
        self.rank = rank
        self._check_invalid()

    def _check_invalid(self) -> str:
        if not isinstance(self.rank, str) or self.rank == "":
            raise TypeError("Your input is invalid")
        if not self.rank in _VALID_RANKS:
            raise ValueError("That's not a rank")
        return self.rank
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return self.rank == other.rank
        else:
            raise AssertionError()
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return _VALID_RANKS.index(self.rank) > _VALID_RANKS.index(other.rank)
        else:
            raise ValueError()

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Rank):
            return _VALID_RANKS.index(self.rank) < _VALID_RANKS.index(other.rank)
        else:
            raise AssertionError()