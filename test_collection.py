
from models.movie_collection import MovieCollection
from utils.storage import MovieStorage

storage = MovieStorage("data/movies.json")
collection = storage.load_movies()

print("\nALL MOVIES")
for movie in collection.get_all_movies():
    print(movie)

print("\nSEARCH RESULTS")
for movie in collection.search_movies("action"):
    print(movie)

print("\nSTATISTICS")
print(collection.get_statistics())

print("\nDELETE MOVIE")
print(collection.delete_movie("The Lion King"))
print("Movies remaining:", len(collection.get_all_movies()))
