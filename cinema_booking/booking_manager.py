from pymongo import ReturnDocument

class BookingManager:
    def __init__(self, bookings_collection):
        self.bookings_collection = bookings_collection

    def booking_id_exists(self, booking_id):
        return bool(self.bookings_collection.find_one({"booking_id": booking_id}))

    def add_booking(self, booking_data):
        self.bookings_collection.insert_one(booking_data)

    def get_all_bookings(self):
        cursor = self.bookings_collection.find()
        return cursor

    def get_booking_by_id(self, booking_id):
        return self.bookings_collection.find_one({"booking_id": booking_id})

    def delete_booking(self, booking_id):
        result = self.bookings_collection.delete_one({"booking_id": booking_id})
        return result.deleted_count > 0

    def update_booking_field(self, booking_id, field, value):
        result = self.bookings_collection.find_one_and_update(
            {"booking_id": booking_id}, 
            {"$set": {field: value}},
            return_document=ReturnDocument.AFTER
            )
        return result