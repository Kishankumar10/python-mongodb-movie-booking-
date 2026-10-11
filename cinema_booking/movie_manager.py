class MovieManager:
    def __init__(self, movies_collection):
        self.movies_collection = movies_collection

    def movie_id_exists(self, movie_id):
        return bool(self.movies_collection.find_one({"movie_id": movie_id}))

    def add_movie(self, movie_data):
        self.movies_collection.insert_one(movie_data)
        