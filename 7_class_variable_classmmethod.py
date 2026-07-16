class Vehicle:
    total_vehicles = 0 # class variable
    
    def __init__(self):
        Vehicle.total_vehicles += 1
    
    @classmethod # classmethod
    def get_total(cls):
        return cls.total_vehicles

v1, v2 = Vehicle(), Vehicle()
print(Vehicle.get_total())
