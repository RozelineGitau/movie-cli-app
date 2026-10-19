
from pathlib import Path

from lib.movie import Movie
from lib.movie_collection import MovieCollection
from lib.storage import MovieStorage


storage = MovieStorage("test_movies.json")
collection = MovieCollection()

movie = Movie("Black Panther", "Ryan Coogler", "Action", 2018)
movie.rating = 9
movie.mark_watched()

collection.add_movie(movie)

# Save the collection
storage.save_movies(collection)
print("Movies saved successfully!")

# Load the collection again
loaded_collection = storage.load_movies()

print("\nLoaded movies:")
for saved_movie in loaded_collection.get_all_movies():
    print(saved_movie)

print("\nTotal loaded:", len(loaded_collection.get_all_movies()))

# Clean up the test file
Path("test_movies.json").unlink(missing_ok=True)
