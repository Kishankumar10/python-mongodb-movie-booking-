from cinema_booking.helpers import get_positive_int, get_date
from datetime import datetime

SHOW_TIME_SLOTS = {
    1: "10:00",
    2: "13:00",
    3: "16:00",
    4: "19:00",
    5: "22:00",
}

def get_show_time():
    print("\n⏰ TIME SLOTS\n")

    for number, time in SHOW_TIME_SLOTS.items():
        print(f"Slot-{number} : {time}")
    print()
    
    while True:
        slot = get_positive_int("Enter time slot number (1-5): ")

        if slot in SHOW_TIME_SLOTS:
            return SHOW_TIME_SLOTS[slot]

        print("❌ Invalid slot number.")

def get_show_date(movie):  
    while True:
        show_date = get_date("Enter show date (dd/mm/yyyy): ")
        if show_date.date() < movie['release_date'].date():
            print(f"📅 Entered date is before the release date({movie['release_date'].strftime('%d-%m-%Y')}), Try again\n")
            continue
        if show_date.date() < datetime.now().date():
            print("❌ You cannot book movie in past\n")
            continue
        return show_date  