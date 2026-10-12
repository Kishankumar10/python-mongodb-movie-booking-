class BookingManager:
    def __init__(self, bookings_collection):
        self.bookings_collection = bookings_collection

    def booking_id_exists(self, booking_id):
        return bool(self.bookings_collection.find_one({"booking_id": booking_id}))

    def add_booking(self, booking_data):
        self.bookings_collection.insert_one(booking_data)