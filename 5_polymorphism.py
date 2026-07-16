class Car:
    def fuel_efficiency(self):
        return 15.5

class Motorcycle:
    def fuel_efficiency(self): # same method name, different behavior
        return 30.0

vehicles = [Car(), Motorcycle()]
for v in vehicles:
    print(v.fuel_efficiency())
