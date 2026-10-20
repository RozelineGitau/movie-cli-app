
import pytest

from models.movie import Movie


def test_movie_creation():
    movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)

    assert movie.title == "Black Panther"
    assert movie.director == "Ryan Coogler"
    assert movie.genre == "Action"
    assert movie.release_year == 2018


def test_movie_rating():
    movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)

    movie.rating = 9

    assert movie.rating == 9


def test_invalid_movie_rating():
    movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)

    with pytest.raises(ValueError):
        movie.rating = 15


def test_watched_status():
    movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)

    assert movie.watched is False

    movie.mark_watched()
    assert movie.watched is True

    movie.mark_unwatched()
    assert movie.watched is False
