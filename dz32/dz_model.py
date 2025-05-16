import pickle
import os.path


class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actor):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actor = actor

    def __str__(self):
        return f'{self.title} ({self.director})'


class MovieModel:
    def __init__(self):
        self.movie = 'movie.txt'
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dick_movie = {
            'название': movie.title,
            'жанр': movie.genre,
            'режиссер': movie.director,
            'год выпуска': movie.year,
            'длительность': movie.duration,
            'студия': movie.studio,
            'актеры': movie.actor
        }
        return dick_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def save_data(self):
        with open(self.movie, 'wb') as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.movie):
            with open(self.movie, 'rb') as f:
                return pickle.load(f)
        else:
            return {}
