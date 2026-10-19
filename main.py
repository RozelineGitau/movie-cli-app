
from lib.movie import Movie
from lib.movie_collection import MovieCollection
from lib.storage import MovieStorage


def display_menu():
    print("\n========== MOVIESHELF ==========")
    print("1. Add Movie")
    print("2. View All Movies")
    print("3. Search Movies")
    print("4. Mark Movie as Watched")
    print("5. Update Movie")
    print("6. Delete Movie")
    print("7. Filter Movies by Genre")
    print("8. View Movie Statistics")
    print("9. Mark Movie as Unwatched")
    print("10. Exit")
    print("================================")


def add_movie(collection, storage):
    print("\n--- Add Movie ---")

    title = input("Enter movie title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    if collection.find_movie(title):
        print("A movie with that title already exists.")
        return

    director = input("Enter director: ").strip()
    genre = input("Enter genre: ").strip()

    if not director or not genre:
        print("Director and genre cannot be empty.")
        return

    try:
        release_year = int(input("Enter release year: "))

        if release_year < 1888:
            print("Release year must be 1888 or later.")
            return

        movie = Movie(title, director, genre, release_year)

        rating_input = input(
            "Enter rating (1-10), or press Enter to skip: "
        ).strip()

        if rating_input:
            movie.rating = float(rating_input)

        collection.add_movie(movie)
        storage.save_movies(collection)
        print("Movie added successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")


def view_movies(collection):
    movies = collection.get_all_movies()

    print("\n--- Your Movies ---")

    if not movies:
        print("Your collection is empty.")
        return

    for number, movie in enumerate(movies, start=1):
        print(f"{number}. {movie}")


def search_movies(collection):
    term = input(
        "Enter title, director, or genre to search: "
    ).strip()

    if not term:
        print("Please enter a search term.")
        return

    results = collection.search_movies(term)

    print("\n--- Search Results ---")

    if results:
        for movie in results:
            print(movie)
    else:
        print("No matching movies found.")


def mark_watched(collection, storage):
    title = input("Enter the exact movie title: ").strip()

    if collection.mark_as_watched(title):
        storage.save_movies(collection)
        print("Movie marked as watched!")
    else:
        print("Movie not found.")


def mark_unwatched(collection, storage):
    title = input("Enter the exact movie title: ").strip()

    if collection.mark_as_unwatched(title):
        storage.save_movies(collection)
        print("Movie marked as unwatched!")
    else:
        print("Movie not found.")


def update_movie(collection, storage):
    title = input(
        "Enter the exact title of the movie to update: "
    ).strip()

    movie = collection.find_movie(title)

    if movie is None:
        print("Movie not found.")
        return

    print("Press Enter to keep an existing value.")

    new_title = input(f"New title [{movie.title}]: ").strip()
    director = input(f"New director [{movie.director}]: ").strip()
    genre = input(f"New genre [{movie.genre}]: ").strip()

    year_input = input(
        f"New release year [{movie.release_year}]: "
    ).strip()

    rating_input = input(
        f"New rating (1-10) [{movie.rating}]: "
    ).strip()

    try:
        release_year = int(year_input) if year_input else None
        rating = float(rating_input) if rating_input else None

        success = collection.update_movie(
            title,
            new_title=new_title or None,
            director=director or None,
            genre=genre or None,
            release_year=release_year,
            rating=rating,
        )

        if success:
            storage.save_movies(collection)
            print("Movie updated successfully!")
        else:
            print("Movie could not be updated.")

    except ValueError as error:
        print(f"Invalid input: {error}")


def delete_movie(collection, storage):
    title = input(
        "Enter the exact title of the movie to delete: "
    ).strip()

    movie = collection.find_movie(title)

    if movie is None:
        print("Movie not found.")
        return

    confirmation = input(
        f"Delete '{movie.title}'? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        collection.delete_movie(title)
        storage.save_movies(collection)
        print("Movie deleted successfully!")
    else:
        print("Deletion cancelled.")


def filter_by_genre(collection):
    genre = input("Enter genre: ").strip()

    if not genre:
        print("Please enter a genre.")
        return

    results = collection.filter_by_genre(genre)

    print(f"\n--- {genre} Movies ---")

    if results:
        for movie in results:
            print(movie)
    else:
        print("No movies found in that genre.")


def view_statistics(collection):
    stats = collection.get_statistics()

    print("\n--- Movie Statistics ---")
    print(f"Total movies: {stats['total_movies']}")
    print(f"Watched: {stats['watched']}")
    print(f"Unwatched: {stats['unwatched']}")
    print(f"Rated movies: {stats['rated_movies']}")
    print(f"Average rating: {stats['average_rating']}")

    print("\nMovies by genre:")

    if stats["genres"]:
        for genre, count in stats["genres"].items():
            print(f"  {genre}: {count}")
    else:
        print("  No movies yet.")

    print("\nMovies by director:")

    if stats["directors"]:
        for director, count in stats["directors"].items():
            print(f"  {director}: {count}")
    else:
        print("  No movies yet.")


def main():
    storage = MovieStorage("movies.json")
    collection = storage.load_movies()

    print("Welcome to MovieShelf!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            add_movie(collection, storage)

        elif choice == "2":
            view_movies(collection)

        elif choice == "3":
            search_movies(collection)

        elif choice == "4":
            mark_watched(collection, storage)

        elif choice == "5":
            update_movie(collection, storage)

        elif choice == "6":
            delete_movie(collection, storage)

        elif choice == "7":
            filter_by_genre(collection)

        elif choice == "8":
            view_statistics(collection)

        elif choice == "9":
            mark_unwatched(collection, storage)

        elif choice == "10":
            storage.save_movies(collection)
            print("Your movies have been saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 10.")


if __name__ == "__main__":
    main()
