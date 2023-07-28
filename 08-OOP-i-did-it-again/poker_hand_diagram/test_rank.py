from rank import Rank
import pytest
from typing import Any

def test_check_invalid_none()-> Any: 
    check_for_type_error(None)
    
def test_Check_invalid_int()-> None:
    check_for_type_error(12)

def test_invalid_empty_string()-> None:
    check_for_value_error("")

def test_invalid_rank()-> None:
    check_for_value_error("1")

def test_valid_rank()-> None:
    result = Rank('10')

def test_compare_equal_rank()-> None:
    assert Rank('7') == Rank('7')

def test_compare_unequel_rank()-> None:
    assert Rank('7') != Rank('8')

def test_unequal_rank_wrong_object_type()-> None:
    check_for_type_error('H' == None)

def test_greater_than()-> None:
    assert Rank('K') > Rank('Q')

def test_not_greater_than()-> None:
    assert not Rank('J') > Rank('K')

def test_lesser_then()-> None:
    assert Rank('J') < Rank('A')

def test_not_lesser_than()-> None:
    assert not Rank('A') < Rank('J')
    

def check_for_type_error(rank: Any) -> None:
    with pytest.raises(TypeError):
        assert Rank(rank)

def check_for_value_error(rank: Any) -> None:
    with pytest.raises(ValueError):
        assert Rank(rank)



