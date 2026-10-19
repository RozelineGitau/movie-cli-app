
from lib.movie import Movie
from lib.movie_collection import MovieCollection


collection = MovieCollection()

movie1 = Movie("Black Panther", "Ryan Coogler", "Action", 2018)
movie1.rating = 9
movie1.mark_watched()

movie2 = Movie("The Lion King", "Jon Favreau", "Adventure", 2019)
movie2.rating = 8

movie3 = Movie("Wonder Woman", "Patty Jenkins", "Action", 2017)

collection.add_movie(movie1)
collection.add_movie(movie2)
collection.add_movie(movie3)

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
