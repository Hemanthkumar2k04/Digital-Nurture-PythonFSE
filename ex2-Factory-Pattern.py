from abc import ABC, abstractmethod

# Main Idea: we create a interface -> we create concrete methods using that interface -> we create a factory that would instantiate
# the required classes


class Vehicle(ABC):

    @abstractmethod
    def drive(self) -> str:
        pass


class Car(Vehicle):
    def drive(self) -> str:
        return "This is the Car class!"


class Truck(Vehicle):
    def drive(self) -> str:
        return "This is a Truck class!"


class MotorCycle(Vehicle):
    def drive(self) -> str:
        return "This is a Motorcycle class!"


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        vehicles = {"car": Car, "truck": Truck, "motorcycle": MotorCycle}

        vehicle_class = vehicles.get(vehicle_type.lower(), None)

        if vehicle_class:
            return vehicle_class()

        raise ValueError(f"Unknown vehicle type: {vehicle_type}")


types = ["car", "truck", "motorcycle", "boat"]

for t in types:
    vehicle = VehicleFactory.get_vehicle(t)
    print(f"{t.capitalize()}: {vehicle.drive()}")

"""
O/P:
Car: This is the Car class!
Truck: This is a Truck class!
Motorcycle: This is a Motorcycle class!
ValueError: Unknown vehicle type: boat
"""
