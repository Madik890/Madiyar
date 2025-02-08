from source import movies
def movies_by_category(category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]