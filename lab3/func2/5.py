from source import movies
from aa4 import average_imdb
from bb3 import movies_by_category
def average_imdb_by_category(category):
    filtered_movies = movies_by_category(category)
    return average_imdb(filtered_movies)