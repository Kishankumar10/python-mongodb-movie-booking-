def format_movie(movie):

    if not movie:
        return "❌ Movie not found"
    
    field_list = [
        f"Movie ID     : {movie['movie_id']}",              
        f"Movie name   : {movie['movie_name']}",
        f"Language     : {movie['language']}",
        f"Genre        : {movie['genre']}",
        f"Duration     : {movie['duration']} minutes",
        f"Release Date : {movie['release_date'].strftime('%d-%m-%Y')}",
        f"Price        : ₹{movie['price']}"
        ]
    return "\n".join(field_list)

def format_booking(booking):

    if not booking:
        return "❌ Booking not found"
    
    field_list = [
        f"Booking ID    : {booking['booking_id']}",
        f"Customer name : {booking['customer_name']}",
        f"Phone number  : {booking['phone_number']}",
        f"Movie ID      : {booking['movie_id']}",
        f"Movie name    : {booking['movie_name']}",
        f"Show date     : {booking['show_date'].strftime('%d-%m-%Y')}",
        f"Show time     : {booking['show_time']}",
        f"Ticket price  : ₹{booking['ticket_price']}",
        f"Tickets       : {booking['tickets']}",
        f"Total amount  : ₹{booking['total_amount']}"
        ]

    return "\n".join(field_list)

def format_compact_movie_list(movie_list):
    divider = '-'*50
    header = (f"\n{divider}\n  ID  | PRICE |  MOVIE NAME\n{divider}")
    body = "\n".join([
        f" {doc['movie_id']} | ₹{doc['price']} | {doc['movie_name']}"
        for doc in movie_list
    ])
    return f"{header}\n{body}\n{divider}"