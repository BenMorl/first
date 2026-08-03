# Flights
# CLASS DEFINITIONS
class Airport():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f"{self.name} Airport is located in {self.location}."


class Airline():
    def __init__(self, name, fleet_size):
        self.name = name
        self.fleet_size = fleet_size

    def get_info(self):
        return f"{self.name} Airline has a fleet size of {self.fleet_size} planes."
    

class Plane():
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def fly(self):
        return f"The {self.model} is flying with a capacity of {self.capacity} passengers."


class Flight():
    def __init__(self, flight_number, origin, destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination

    def get_info(self):
        return f"Flight {self.flight_number} is flying from {self.origin} to {self.destination}."


class Seat():
    def __init__(self, seat_number, seat_class):
        self.seat_number = seat_number
        self.seat_class = seat_class

    def get_info(self):
        return f"Seat {self.seat_number} is in {self.seat_class} class."
    

class Passenger():
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def get_info(self):
        return f"Passenger {self.name} with passport number {self.passport_number}."

    