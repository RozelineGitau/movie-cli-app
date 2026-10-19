# movie-cli-app
Group 6 PT15 software engineering movie-cli project
# MovieShelf 🎬

MovieShelf is a menu-based command-line application built with Python that helps users manage their personal movie collections. Users can add movies, search for them, update details, track watched status, and view collection statistics. Movie information is saved in a JSON file so it remains available when the application is restarted.

## Features

- **Add Movies:** Store movie titles, directors, genres, release years, and optional ratings.
- **View Movies:** Display all movies in the collection.
- **Search Movies:** Find movies by title, director, or genre.
- **Track Watched Status:** Mark movies as watched or unwatched.
- **Update Movies:** Edit existing movie information.
- **Delete Movies:** Remove movies from the collection.
- **Filter by Genre:** Display movies belonging to a specific genre.
- **View Statistics:** See the total number of movies, watched and unwatched counts, movies by genre and director, and average rating.
- **Data Persistence:** Save and load movie information using JSON.
- **Input Validation:** Handle invalid choices, missing information, and invalid ratings.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON for data storage
- `pathlib` for file handling
- Git and GitHub for version control and collaboration

## Project Structure

```
├── data
│   └── movies.json
├── main.py
├── models
│   ├── __init__.py
│   ├── media.py
│   ├── movie_collection.py
│   └── movie.py
├── README.md
├── requirements.txt
├── test_collection.py
├── test_movie.py
├── test_storage.py
└── utils
    ├── __init__.py
    └── storage.py
```

## Getting Started

### Prerequisites

Install Python 3 on your computer.

Check your Python version:

```bash
python3 --version
```

### Installation

1. Clone the repository or download the project.
2. Navigate to the project directory:

```bash
cd movie-cli-app
```

3. Run the application:

```bash
python3 main.py
```

## How to Use

When the application starts, a menu appears with the available operations:

1. Add Movie
2. View All Movies
3. Search Movies
4. Mark Movie as Watched
5. Update Movie
6. Delete Movie
7. Filter Movies by Genre
8. View Movie Statistics
9. Mark Movie as Unwatched
10. Exit

Enter the number corresponding to the operation you want to perform and follow the prompts.

Movie details are stored in `movies.json` and loaded when the application starts again.


## Learning Objectives

This project demonstrates practical application of:

- Classes, objects, inheritance, and encapsulation
- Properties and validation
- Lists, dictionaries, and class attributes
- CRUD operations (Create, Read, Update, Delete)
- File handling and JSON serialization
- Modular Python development
- Testing and version control

## Future Improvements

- Add sorting by title, year, or rating.
- Support exporting movie statistics.
- Improve automated test coverage.
- Add a graphical user interface.

## Author

Group 6
