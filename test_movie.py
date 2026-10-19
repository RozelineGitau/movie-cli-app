
from lib.movie import Movie


movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)

print(movie)
print("Title:", movie.title)
print("Director:", movie.director)
print("Total movies:", Movie.count)
print("Genres:", Movie.genres)

movie.rating = 9
movie.mark_watched()

print("Updated movie:", movie)

try:
    movie.rating = 15
except ValueError as error:
    print("Validation:", error)
