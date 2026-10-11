from pymongo import ReturnDocument

class MovieManager:
    def __init__(self, movies_collection):
        self.movies_collection = movies_collection

    def movie_id_exists(self, movie_id):
        return bool(self.movies_collection.find_one({"movie_id": movie_id}))

    def add_movie(self, movie_data):
        self.movies_collection.insert_one(movie_data)

    def get_all_movies(self):
        cursor = self.movies_collection.find()
        return cursor
    
    def get_movie_by_id(self, movie_id):
        return self.movies_collection.find_one({"movie_id": movie_id})

    def get_movie_by_name(self, movie_name):
        return self.movies_collection.find_one({"movie_name": movie_name})

    def delete_movie(self, movie_id):
        result = self.movies_collection.delete_one({"movie_id": movie_id})
        return result.deleted_count > 0

    def update_movie_field(self, movie_id, field, value):
        result = self.movies_collection.find_one_and_update(
            {"movie_id": movie_id}, 
            {"$set": {field: value}},
            return_document=ReturnDocument.AFTER
            )
        return result