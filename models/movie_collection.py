
from models.movie import Movie


class MovieCollection:
    def __init__(self):
        self._movies = []

    @property
    def movies(self):
        return self._movies.copy()

    def add_movie(self, movie):
        if not isinstance(movie, Movie):
            raise TypeError("Only Movie objects can be added.")

        self._movies.append(movie)

    def get_all_movies(self):
        return self.movies

    def find_movie(self, title):
        for movie in self._movies:
            if movie.title.lower() == title.lower():
                return movie

        return None

    def search_movies(self, search_term):
        search_term = search_term.lower()

        return [
            movie for movie in self._movies
            if search_term in movie.title.lower()
            or search_term in movie.director.lower()
            or search_term in movie.genre.lower()
        ]

    def filter_by_genre(self, genre):
        return [
            movie for movie in self._movies
            if movie.genre.lower() == genre.lower()
        ]

    def update_movie(self, title, new_title=None,
                     director=None, genre=None,
                     release_year=None, rating=None):
        movie = self.find_movie(title)

        if movie is None:
            return False

        if new_title is not None:
            movie._title = new_title

        if director is not None:
            movie._director = director

        if genre is not None:
            movie._genre = genre

        if release_year is not None:
            if not isinstance(release_year, int) or isinstance(release_year, bool):
                raise ValueError("Release year must be a whole number.")
            if release_year < 1888:
                raise ValueError("Release year must be 1888 or later.")
            movie._release_year = release_year

        if rating is not None:
            movie.rating = rating

        return True

    def delete_movie(self, title):
        movie = self.find_movie(title)

        if movie is None:
            return False

        self._movies.remove(movie)
        return True

    def mark_as_watched(self, title):
        movie = self.find_movie(title)

        if movie is None:
            return False

        movie.mark_watched()
        return True

    def mark_as_unwatched(self, title):
        movie = self.find_movie(title)

        if movie is None:
            return False

        movie.mark_unwatched()
        return True

    def get_statistics(self):
        genre_count = {}
        director_count = {}
        rated_movies = [
            movie for movie in self._movies
            if movie.rating is not None
        ]

        for movie in self._movies:
            genre_count[movie.genre] = (
                genre_count.get(movie.genre, 0) + 1
            )
            director_count[movie.director] = (
                director_count.get(movie.director, 0) + 1
            )

        average_rating = (
            sum(movie.rating for movie in rated_movies)
            / len(rated_movies)
            if rated_movies else 0
        )

        return {
            "total_movies": len(self._movies),
            "watched": sum(movie.watched for movie in self._movies),
            "unwatched": sum(not movie.watched for movie in self._movies),
            "genres": genre_count,
            "directors": director_count,
            "rated_movies": len(rated_movies),
            "average_rating": round(average_rating, 2),
        }
