from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# ==========================================
# CLASS DEFINITIONS
# ==========================================

class Airport:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} Airport is located in {self.location}."


class Airline:
    def __init__(self, name: str, fleet_size: int):
        self.name = name
        self.fleet_size = fleet_size
        self.destinations = [
            "Sydney",
            "New York",
            "London",
            "Tokyo",
            "Melbourne",
            "Gold Coast",
            "Los Angeles",
            "Singapore",
            "Dubai",
            "Hong Kong"
        ]

    def get_info(self):
        return f"{self.name} Airline has a fleet size of {self.fleet_size} planes."

    def show_destinations(self):
        print("\nAvailable destinations:")

        for index, destination in enumerate(self.destinations, start=1):
            print(f"{index}. {destination}")


class Plane:
    def __init__(self, model: str, capacity: int):
        self.model = model
        self.capacity = capacity

    def fly(self):
        return f"The {self.model} is flying with a capacity of {self.capacity} passengers."

    def get_info(self):
        return f"Plane: {self.model} | Capacity: {self.capacity} passengers."


class Flight:
    def __init__(
        self,
        flight_number: str,
        origin: Airport,
        destination: Airport,
        plane: Plane,
        airline: Airline
    ):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.plane = plane
        self.airline = airline

    def get_info(self):
        return (
            f"Flight {self.flight_number}: "
            f"{self.origin.location} -> {self.destination.location}"
        )

    def calculate_distance(self) -> float:
        geolocator = Nominatim(user_agent="flight_system")

        origin_location = geolocator.geocode(self.origin.location)
        destination_location = geolocator.geocode(self.destination.location)

        if origin_location and destination_location:

            origin_coords = (
                origin_location.latitude,
                origin_location.longitude
            )

            destination_coords = (
                destination_location.latitude,
                destination_location.longitude
            )

            distance = geodesic(
                origin_coords,
                destination_coords
            ).kilometers

            return distance

        raise ValueError("Could not find the specified locations.")


class Seat:
    def __init__(self, seat_number: str, seat_class: str):
        self.seat_number = seat_number
        self.seat_class = seat_class

    def get_info(self):
        return f"Seat {self.seat_number} is in {self.seat_class} class."


class Passenger:
    def __init__(self, name: str, passport_number: str):
        self.name = name
        self.passport_number = passport_number

    def get_info(self):
        return (
            f"Passenger: {self.name} | "
            f"Passport: {self.passport_number}"
        )


class Booking:
    def __init__(self, passenger: Passenger, flight: Flight, seat: Seat):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.status = "Pending"
        self.check_in_status = False

    def confirm_booking(self):
        self.status = "Confirmed"

    def check_in(self):
        if self.status == "Confirmed":
            self.check_in_status = True
            return True

        return False

    def get_info(self):
        return (
            f"\n===== BOOKING =====\n"
            f"Passenger: {self.passenger.name}\n"
            f"Flight: {self.flight.flight_number}\n"
            f"Route: {self.flight.origin.location} -> "
            f"{self.flight.destination.location}\n"
            f"Seat: {self.seat.seat_number}\n"
            f"Class: {self.seat.seat_class}\n"
            f"Status: {self.status}\n"
            f"Check-in: "
            f"{'Completed' if self.check_in_status else 'Pending'}"
        )


# ==========================================
# INPUT FUNCTIONS
# ==========================================

def input_option() -> str:
    return input("Select an option: ")


def input_passenger_name() -> str:
    return input("Enter the passenger name: ")


def input_passport_number() -> str:
    return input("Enter the passport number: ")


def input_destination(airline: Airline) -> str:

    airline.show_destinations()

    while True:
        try:
            option = int(input("Choose your destination: "))

            if 1 <= option <= len(airline.destinations):
                return airline.destinations[option - 1]

            print("Invalid destination.")

        except ValueError:
            print("Please enter a valid number.")


def input_seat() -> Seat:

    print("\nAvailable seats:")
    print("1. 12A - Economy")
    print("2. 12B - Economy")
    print("3. 13A - Economy")
    print("4. 1A  - Business")

    while True:
        try:
            option = int(input("Choose your seat: "))

            match option:
                case 1:
                    return Seat("12A", "Economy")

                case 2:
                    return Seat("12B", "Economy")

                case 3:
                    return Seat("13A", "Economy")

                case 4:
                    return Seat("1A", "Business")

                case _:
                    print("Invalid seat.")

        except ValueError:
            print("Please enter a valid number.")


# ==========================================
# BOOKING PROCESS
# ==========================================

def book_flight(airline: Airline, plane: Plane, origin: Airport):

    print("\n===== BOOK FLIGHT =====")

    # Choose destination
    destination_name = input_destination(airline)

    destination = Airport(
        f"{destination_name} Airport",
        destination_name
    )

    # Create flight
    flight = Flight(
        "QF800",
        origin,
        destination,
        plane,
        airline
    )

    print("\nFlight selected:")
    print(flight.get_info())

    # Calculate distance
    try:
        distance = flight.calculate_distance()
        print(f"Distance: {distance:.2f} km")

    except ValueError as error:
        print(error)

    # Passenger information
    print("\n===== PASSENGER INFORMATION =====")

    name = input_passenger_name()
    passport = input_passport_number()

    passenger = Passenger(
        name,
        passport
    )

    # Choose seat
    seat = input_seat()

    # Create booking
    booking = Booking(
        passenger,
        flight,
        seat
    )

    # Confirm booking
    booking.confirm_booking()

    print("\nBooking successfully confirmed!")

    print(booking.get_info())

    return booking


# ==========================================
# MENU
# ==========================================

def menu():

    print("\n===== FLIGHT SYSTEM =====")
    print("1. Book a flight")
    print("2. Check-in")
    print("3. View booking")
    print("4. Exit")


# ==========================================
# MAIN
# ==========================================

def main():

    # Create airport
    origin = Airport(
        "Santiago International",
        "Santiago, Chile"
    )

    # Create airline
    airline = Airline(
        "Qantas",
        200
    )

    # Create plane
    plane = Plane(
        "Boeing 787 Dreamliner",
        416
    )

    # No booking exists initially
    booking = None

    while True:

        menu()

        option = input_option()

        match option:

            case "1":

                booking = book_flight(
                    airline,
                    plane,
                    origin
                )

            case "2":

                if booking is None:

                    print("\nYou don't have a booking yet.")

                else:

                    if booking.check_in():

                        print(
                            f"\nCheck-in completed for "
                            f"{booking.passenger.name}."
                        )

                    else:

                        print(
                            "\nYou must confirm your booking "
                            "before checking in."
                        )

            case "3":

                if booking is None:

                    print("\nYou don't have a booking yet.")

                else:

                    print(booking.get_info())

            case "4":

                print(
                    f"\nThanks for using "
                    f"{airline.name} Airlines!"
                )

                break

            case _:

                print(
                    "\nInvalid option. "
                    "Please try again."
                )


if __name__ == "__main__":
    main()

