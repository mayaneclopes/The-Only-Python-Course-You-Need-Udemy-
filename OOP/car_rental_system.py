# Vehicle Rental System
# You are designing a Vehicle Rental System that tracks different types of vehicles and their components.
# Tasks:
# Create a class Engine with an attribute horsepower and a method get_engine_info() that returns "150 HP Engine".
# Create class Vehicle
# Attributes: brand, model, and an Engine object.
# Class attribute: total_vehicles (increased by 1 each time a new vehicle is created).
# Add a method get_details() returning brand, model, and engine info.
# Add @staticmethod get_vehicle_type() → returns "Generic Vehicle".
# Add @classmethod get_total_vehicles() → returns total number of vehicles.
# Add a @property rental_price and corresponding setter that ensures the value is non-negative.-
# Create a Car class that inherits from Vehicle.
# Add an attribute seats.
# Override the get_details() method and use super() to include base details and append "Seats: X".

class Engine:
    def __init__(self, horsepower=150):
        self.horsepower = horsepower

    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"


class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, engine_obj, rental_price=0.0):
        self.brand = brand
        self.model = model
        self.engine = engine_obj
        self.rental_price = rental_price  # Isso ativa o setter abaixo
        Vehicle.total_vehicles += 1

    def get_details(self):
        return f"{self.brand} {self.model}, {self.engine.get_engine_info()}"

    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @property
    def rental_price(self):
        return self._rental_price

    @rental_price.setter
    def rental_price(self, value):
        if value < 0:
            raise ValueError("Rental price can't be negative!")
        self._rental_price = value


class Car(Vehicle):
    def __init__(self, brand, model, engine_obj, seats, rental_price=0.0):
        super().__init__(brand, model, engine_obj, rental_price)
        self.seats = seats

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Seats: {self.seats}"


# TESTS

# Creating engine
motor_v8 = Engine(150)

# Creating vehicle
veiculo = Vehicle("Ford", "Transit", motor_v8, 120.0)
print(veiculo.get_details())  # Ford Transit, 150 HP Engine

# Creating a car
carro = Car("Toyota", "Corolla", motor_v8, seats=5, rental_price=150.0)
print(carro.get_details())  # Toyota Corolla, 150 HP Engine, Seats: 5

# Testing decorators
print("Vehicle type:", Vehicle.get_vehicle_type())  # Generic Vehicle
print("Total vehicles created:", Vehicle.get_total_vehicles())  # 2

# Testing price validation
try:
    carro.rental_price = -10  
except ValueError as e:
    print("Error:", e)