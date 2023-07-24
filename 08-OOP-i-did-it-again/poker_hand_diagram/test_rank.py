from rank import Rank
import pytest

def test_check_invalid_none()-> None: 
    with pytest.raises(TypeError):
        assert Rank(None)
    
def test_Check_invalid_int()-> None:
    with pytest.raises(TypeError):
        assert Rank(12)

def test_invalid_empty_string()-> None:
    with pytest.raises(TypeError):
        assert Rank("")

def test_invalid_rank()-> None:
    with pytest.raises(ValueError):
        assert Rank("1")

def test_valid_rank()-> None:
    result = Rank('10')

def test_compare_equal_rank()-> None:
    assert Rank('7') == Rank('7')

def test_compare_unequel_rank()-> None:
    assert Rank('7') != Rank('8')

def test_unequal_rank_error()-> None:
    with pytest.raises(AssertionError):
        assert Rank('6') == ('J')

def test_greater_than()-> None:
    assert Rank('K') > Rank('Q')

def test_not_greater_than_error()-> None:
    with pytest.raises(ValueError):
        Rank('J') > ('K')

def test_lesser_then()-> None:
    assert Rank('J') < Rank('A')

def test_not_lesser_than_error()-> None:
    with pytest.raises(AssertionError):
        assert Rank('A') < Rank('J')



