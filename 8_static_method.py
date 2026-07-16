class Vehicle:
    @staticmethod # static method
    def is_eco_friendly(efficiency):
        return efficiency >= 18

print(Vehicle.is_eco_friendly(20))
