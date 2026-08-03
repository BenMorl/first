# Flights
# CLASS DEFINITIONS
class Airport():
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} Airport is located in {self.location}."


class Airline():
    def __init__(self, name: str, fleet_size: int):
        self.name = name
        self.fleet_size = fleet_size

    def get_info(self):
        return f"{self.name} Airline has a fleet size of {self.fleet_size} planes."
    
    
class Plane():
    def __init__(self, model: str, capacity: int):
        self.model = model
        self.capacity = capacity

    def fly(self):
        return f"The {self.model} is flying with a capacity of {self.capacity} passengers."


class Flight():
    def __init__(self, flight_number: str, origin: str, destination: str):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination

    def get_info(self):
        return f"Flight {self.flight_number} is flying from {self.origin} to {self.destination}."


class Booking():
    def __init__(self, flight: Flight, passenger: 'Passenger', seat: 'Seat'):
        self.flight = flight
        self.passenger = passenger
        self.seat = seat

    def get_info(self):
        return f"Booking for {self.passenger.name} on flight {self.flight.flight_number} at seat {self.seat.seat_number}."
    

class Seat():
    def __init__(self, seat_number: int, seat_class: str):
        self.seat_number = seat_number
        self.seat_class = seat_class

    def get_info(self):
        return f"Seat {self.seat_number} is in {self.seat_class} class."
    

class Passenger():
    def __init__(self, name: str, passport_number: str):
        self.name = name
        self.passport_number = passport_number

    def get_info(self):
        return f"Passenger {self.name} with passport number {self.passport_number}."



# OTHER FUNCTIONS
def input_option() -> str:
    option = input("select an option (1-7): ")
    return option


# MENU AND MAIN
def menu():
    print("\n===== FLIGHT SYSTEM =====")
    print("1. View airport information")
    print("2. View airline information")
    print("3. View flight information")
    print("4. View plane information")
    print("5. View passenger information")
    print("6. Book a seat")
    print("7. Check-in passenger")
    print("8. Depart flight")
    print("9. Exit")


def main():
    # Create instances of each class
    airport = Airport("JFK", "New York")
    airline = Airline("Delta", 200)
    plane = Plane("Boeing 747", 416)
    flight = Flight("DL123", "New York", "Los Angeles")
    seat = Seat(12, "Economy")
    passenger = Passenger("John Doe", "A12345678")

    while True:
        menu()
        option = input_option()
        match option:
            case "1":
                print(airport.get_info())
            case "2":
                print(airline.get_info())
            case "3":
                print(plane.get_info())
            case "4":
                print(flight.get_info())
            case "5":
                print(seat.get_info())
            case "6":
                print(passenger.get_info())
            case "7":
                print("Exiting...")
            case "8":
                print("Exiting...")
            case "9":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")