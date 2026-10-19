
class Media:
    def __init__(self, title, genre, release_year):
        self._title = title
        self._genre = genre
        self._release_year = release_year

    @property
    def title(self):
        return self._title

    @property
    def genre(self):
        return self._genre

    @property
    def release_year(self):
        return self._release_year
