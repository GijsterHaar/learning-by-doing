from cards_object import Card
import pytest

def test_exist():
    result = Card("2D")

def test_rank_int():
    result = Card('5H')
    assert result.rank == "5"

def test_rank_char():
    result = Card("JH")
    assert result.rank == "jack"

def test_suit():
    result = Card("JH")
    assert result.suit == "hearts"

def test_rank_ten():
    result = Card("10D")
    assert result.rank == "10"

def test_description():
    result = Card("JH")
    assert result.description == "a jack of hearts"

def test_rank_invalid():
    with pytest.raises(KeyError):
        result = Card("1H")

def test_suit_invalid():
    with pytest.raises(KeyError):
        result = Card("2L")

def test_empty_string():
    with pytest.raises(KeyError):
        result = Card("")

def test_wrong_input_integer():
    with pytest.raises(TypeError):
        result = Card(2)

def test_wrong_input_None():
    with pytest.raises(TypeError):
        result = Card(None)


