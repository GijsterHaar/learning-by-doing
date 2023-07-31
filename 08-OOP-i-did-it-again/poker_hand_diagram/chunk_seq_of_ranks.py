
from typing import List, Any

class Chunk:
    def __init__(self, seq: object) -> None:
        self._seq = seq
        self.__rank_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__rank_size = 5
        self._ranks_straight = [self.__rank_order[rank:rank + self.__rank_size] for rank in range(0, 10)]
        self._ranks_straight_flush = [self.__rank_order[rank:rank + self.__rank_size] for rank in range(0, 9)]
        self._ranks_royal_flush = self.__rank_order[9:]
        self.sorted_straight_ranks = self._sort_straight_ranks()
        self.sorted_straight_ranks_flush = self._sort_straight_ranks_flush()
        self.sorted_straight_ranks_royal_flush = self._sort_royal_flush()
        
    
    def _sort_straight_ranks(self) -> object:
        for straight_ranks in self._ranks_straight:
            straight_ranks.sort()
        return self._ranks_straight
        
    def _sort_straight_ranks_flush(self) -> object:
        for straight_ranks_flush in self._ranks_straight_flush:
            straight_ranks_flush.sort()
        return self._ranks_straight_flush
        
    def _sort_royal_flush(self) -> object:
        return self._ranks_royal_flush.sort()
    
    def _find_seq_in_straight_ranks(self) -> str:
        if self._seq in self._ranks_straight:
            return 'Straight'
        
    def _find_seq_in_straight_ranks_flush(self) -> str:
        if self._seq in self._ranks_straight_flush:
            return 'Straight Flush'
    
    def _find_royal_flush(self) -> str:
        if self._seq == self._ranks_royal_flush:
            return 'Royal Flush'