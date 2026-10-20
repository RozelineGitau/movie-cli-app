
import json

from models.movie import Movie
from models.movie_collection import MovieCollection
from utils.storage import MovieStorage


def test_save_movies(tmp_path):
    file_path = tmp_path / "movies.json"
    storage = MovieStorage(str(file_path))

    collection = MovieCollection()
    movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)
    movie.rating = 9
    movie.mark_watched()
    collection.add_movie(movie)

    storage.save_movies(collection)

    assert file_path.exists()

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["title"] == "Black Panther"
    assert data[0]["rating"] == 9
    assert data[0]["watched"] is True


def test_load_movies(tmp_path):
    file_path = tmp_path / "movies.json"

    data = [
        {
            "title": "Black Panther",
            "director": "Ryan Coogler",
            "genre": "Action",
            "release_year": 2018,
            "rating": 9,
            "watched": True,
        }
    ]

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file)

    storage = MovieStorage(str(file_path))
    collection = storage.load_movies()

    movies = collection.get_all_movies()

    assert len(movies) == 1
    assert movies[0].title == "Black Panther"
    assert movies[0].rating == 9
    assert movies[0].watched is True


def test_load_missing_file(tmp_path):
    file_path = tmp_path / "missing.json"
    storage = MovieStorage(str(file_path))

    collection = storage.load_movies()

    assert collection.get_all_movies() == []
