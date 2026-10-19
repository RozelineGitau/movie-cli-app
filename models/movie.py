
from models.media import Media


class Movie(Media):
    # Class attributes shared by all Movie objects
    count = 0
    genres = []
    directors = []
    genre_count = {}
    director_count = {}

    def __init__(self, title, director, genre, release_year):
        super().__init__(title, genre, release_year)

        self._director = director
        self._rating = None
        self._watched = False

        Movie.count += 1

        if genre not in Movie.genres:
            Movie.genres.append(genre)

        if director not in Movie.directors:
            Movie.directors.append(director)

        Movie.genre_count[genre] = (
            Movie.genre_count.get(genre, 0) + 1
        )

        Movie.director_count[director] = (
            Movie.director_count.get(director, 0) + 1
        )

    @property
    def director(self):
        return self._director

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value is not None and (
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not 1 <= value <= 10
        ):
            raise ValueError("Rating must be between 1 and 10.")

        self._rating = value

    @property
    def watched(self):
        return self._watched

    def mark_watched(self):
        self._watched = True

    def mark_unwatched(self):
        self._watched = False

    def __str__(self):
        status = "Watched" if self.watched else "Not watched"
        rating = self.rating if self.rating is not None else "Not rated"

        return (
            f"{self.title} ({self.release_year}) | "
            f"Director: {self.director} | "
            f"Genre: {self.genre} | "
            f"Rating: {rating} | Status: {status}"
        )
