class Vehicle: # Parent
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle): # Single Inheritance
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

class SportsCar(Car): # Multilevel Inheritance
    def __init__(self, brand, doors, speed):
        super().__init__(brand, doors)
        self.speed = speed

s = SportsCar("Ferrari", 2, 330)
print(s.brand, s.doors, s.speed)
