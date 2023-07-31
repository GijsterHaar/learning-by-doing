from chunk_seq_of_ranks import Chunk
import pytest

def test_seq_in_straight_ranks() -> None:
    result = Chunk([' 3', '5', '6', ' 4', '7'])
    result._find_seq_in_straight_ranks() == 'Straight'

def test_seq_in_straight_ranks_flush() -> None:
    result = Chunk([' 3', '5', '6', ' 4', '7'])
    result._find_seq_in_straight_ranks_flush() == 'Straight Flush'

def testing_seq_royal_flush() -> None:
    result = Chunk(['10', 'A', 'J', 'Q', 'K'], )
    result._sort_royal_flush()  == 'Royal Flush'