

class Chunk:
    def __init__(self):
        self.__rank_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__chunk_size = 5
        self._chunked_straight = [self.__rank_order[rank:rank + self.__chunk_size] for rank in range(0, 10)]
        self._chunked_straight_flush = [self.__rank_order[rank:rank + self.__chunk_size] for rank in range(0, 9)]
        self._rank_royal_flush = self.__rank_order[9:]
        self._rank_royal_flush.sort()