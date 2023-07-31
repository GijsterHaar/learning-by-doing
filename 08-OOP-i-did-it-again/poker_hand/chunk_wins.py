

class Chunk:
    def __init__(self):
        self.__rank_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__rank_size = 5
        self._ranks_straight = [self.__rank_order[rank:rank + self.__rank_size] for rank in range(0, 10)]
        self._ranks_straight_flush = [self.__rank_order[rank:rank + self.__rank_size] for rank in range(0, 9)]
        self._ranks_royal_flush = self.__rank_order[9:]
        self._sort_all_ranks()
        
    
    def _sort_all_ranks(self):
        for straight_ranks in self._ranks_straight:
            return straight_ranks.sort()
        for straight_ranks_flush in self._ranks_straight_flush:
            return straight_ranks_flush.sort()
        return self._ranks_royal_flush.sort()
    
