from card import Card
import pytest


def test_check_invalid_none()-> None:
    with pytest.raises(TypeError):
        assert Card(None)

def test_check_invalid_int()-> None:
    with pytest.raises(TypeError):
        assert Card(12)

def test_invalid_empty_string()-> None:
    with pytest.raises(ValueError):
        assert Card("")

def test_invalid_rank()-> None:
    with pytest.raises(ValueError):
        assert Card("1C")

def test_valid_rank()-> None:
    result = Card('10C')

def test_invalid_unknown_suit() -> None:
    with pytest.raises(ValueError):
        result = Card("7A")

def test_valid_suit() -> None:
    result = Card("7H")

def test_compare_equal_rank()-> None:
    assert Card('7H') == Card('7C')

def test_compare_unequel_rank()-> None:
    assert Card('7D') != Card('8H')

def test_equality_wrong_object_type() -> None:
    with pytest.raises(TypeError):
        assert Card('7H') == None

def test_greater_than()-> None:
    assert Card('KH') > Card('QC')

def test_not_greater_than()-> None:
    assert not Card('JC') > Card('KH')

def test_lesser_then()-> None:
    assert Card('JH') < Card('AC')

def test_not_lesser_than()-> None:
    assert not Card('AD') < Card('JH')