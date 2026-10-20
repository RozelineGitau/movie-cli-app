
from models.movie import Movie
from models.movie_collection import MovieCollection


def create_collection():
    collection = MovieCollection()
    collection.add_movie(
        Movie("Black Panther", "Ryan Coogler", "Action", 2018)
    )
    collection.add_movie(
        Movie("Iron Man", "Jon Favreau", "Action", 2008)
    )
    collection.add_movie(
        Movie("Wonder Woman", "Patty Jenkins", "Adventure", 2017)
    )
    return collection


def test_add_and_get_movies():
    collection = create_collection()

    assert len(collection.get_all_movies()) == 3


def test_find_movie():
    collection = create_collection()

    movie = collection.find_movie("black panther")

    assert movie is not None
    assert movie.title == "Black Panther"


def test_search_movies():
    collection = create_collection()

    results = collection.search_movies("Action")

    assert len(results) == 2


def test_filter_by_genre():
    collection = create_collection()

    results = collection.filter_by_genre("Adventure")

    assert len(results) == 1
    assert results[0].title == "Wonder Woman"


def test_delete_movie():
    collection = create_collection()

    result = collection.delete_movie("Iron Man")

    assert result is True
    assert len(collection.get_all_movies()) == 2
    assert collection.find_movie("Iron Man") is None


def test_movie_statistics():
    collection = create_collection()

    stats = collection.get_statistics()

    assert stats["total_movies"] == 3
    assert stats["genres"]["Action"] == 2
    assert stats["genres"]["Adventure"] == 1
    assert stats["directors"]["Ryan Coogler"] == 1
