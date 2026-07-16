class ElectricCar:
    def __init__(self, battery):
        self.battery = battery
    
    def __add__(self, other): # operator overloading
        return self.battery + other.battery

ev1 = ElectricCar(75)
ev2 = ElectricCar(75)
print(ev1 + ev2) # 150
