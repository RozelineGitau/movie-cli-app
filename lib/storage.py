
import json
from pathlib import Path

from lib.movie import Movie
from lib.movie_collection import MovieCollection


class MovieStorage:
    def __init__(self, filename="movies.json"):
        self.filename = Path(filename)

    def save_movies(self, collection):
        movies_data = []

        for movie in collection.get_all_movies():
            movies_data.append({
                "title": movie.title,
                "director": movie.director,
                "genre": movie.genre,
                "release_year": movie.release_year,
                "rating": movie.rating,
                "watched": movie.watched,
            })

        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(movies_data, file, indent=4)

    def load_movies(self):
        collection = MovieCollection()

        if not self.filename.exists():
            return collection

        with self.filename.open("r", encoding="utf-8") as file:
            movies_data = json.load(file)

        for data in movies_data:
            movie = Movie(
                data["title"],
                data["director"],
                data["genre"],
                data["release_year"],
            )

            movie.rating = data["rating"]

            if data["watched"]:
                movie.mark_watched()

            collection.add_movie(movie)

        return collection
