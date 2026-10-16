import os
from pymongo import MongoClient
from dotenv import load_dotenv

def connect_to_database():

    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")

    if not mongo_uri:
        raise RuntimeError("MONGO_URI is missing. Check your .env file.")
    client = MongoClient(mongo_uri)

    try:
        db = client["Movie_DB"]
        movies_collection = db["movies"]
        bookings_collection = db["bookings"]

        movies_collection.create_index("movie_id", unique=True)
        bookings_collection.create_index("booking_id", unique=True)

        return client, db, movies_collection, bookings_collection

    except Exception:
        client.close()
        raise