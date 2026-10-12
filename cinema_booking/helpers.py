# Helper functions

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("❌ Input cannot be empty, Try again\n")
            continue
        return value

def get_positive_int(prompt):
    while True: 
        try:
            value = int(get_input(prompt))
            if value <= 0:
                print("❌ Value must be greater than 0\n")
                continue
            return value
        except ValueError:
            print("❌ Invalid input, Enter a valid integer\n")

def get_positive_float(prompt):
    while True: 
        try:
            value = float(get_input(prompt))
            if value <= 0:
                print("❌ Value must be greater than 0\n")
                continue
            return value
        except ValueError:
            print("❌ Invalid input, Enter a valid number\n")