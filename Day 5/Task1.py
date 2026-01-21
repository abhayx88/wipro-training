# Base class
class Vehicle:
    # Class variable to track number of vehicles
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")


# Single Inheritance
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")


# Multilevel Inheritance
class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


# Creating objects
v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

# Calling methods
v1.start()
c1.start()
c1.drive()
e1.start()
e1.drive()
e1.charge()

# Accessing class variable
print("Total vehicles created:", Vehicle.vehicle_count)
