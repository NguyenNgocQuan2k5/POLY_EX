import os
os.system('cls')

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = self.fuel_consumption + 0.9
        required_fuel = total_consumption * distance
        
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel
        else:
            print("Car cannot drive the given distance. Fuel remains unchanged.")

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        
        total_consumption = self.fuel_consumption + 1.6
        required_fuel = total_consumption * distance
        
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel
        else:
            print("Truck cannot drive the given distance. Fuel remains unchanged.")

    def refuel(self, fuel):
        effective_fuel = fuel * 0.95  
        self.fuel_quantity += effective_fuel
        return self.fuel_quantity


if __name__ == "__main__":
    car = Car(20, 5)
    car.drive(3)
    print(car.fuel_quantity)
    car.refuel(10)
    print(car.fuel_quantity)
    truck = Truck(100, 15)
    truck.drive(5)
    print(truck.fuel_quantity)
    truck.refuel(50)
    print(truck.fuel_quantity)

