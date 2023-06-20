from movie_OOP import Movie
import pytest

def test_find_Movie():
    result = Movie

def test_movie_construction():
    result = Movie('lamaland', [], 2025, "nobody knows", 10)
    assert result.title == 'lamaland'
    assert result.actors == []
    assert result.year == 2025
    assert result.genre == 'nobody knows'
    assert result.rating == 10

def test_string_method():
    movie = Movie('lamaland', [], 2025, "nobody knows", 10)
    result = str(movie)
    assert result == 'lamaland, 10'

def test_lt_method():
    movie = Movie('lamaland', [], 2025, "nobody knows", 9)
    movie_2 = Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10)
    assert movie < movie_2

def test_lt_method_other_way_round():
    movie = Movie('lamaland', [], 2025, "nobody knows", 9)
    movie_2 = Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10)
    assert not movie_2 < movie

def test_lt_method_again():
    movie = Movie('lamaland', [], 2025, "nobody knows", 9)
    movie_2 = Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10)
    with pytest.raises(TypeError):
        assert movie < 19