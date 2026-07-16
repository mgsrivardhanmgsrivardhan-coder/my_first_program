from abc import ABC, abstractmethod

class Vehicle(ABC): # Abstract class
    @abstractmethod
    def fuel_efficiency(self):
        pass

class Car(Vehicle):
    def fuel_efficiency(self): # must implement
        return 15.5

c = Car()
print(c.fuel_efficiency())
