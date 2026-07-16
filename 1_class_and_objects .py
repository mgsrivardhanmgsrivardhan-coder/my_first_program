class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describe(self):
        return f"{self.brand} {self.model}"

# OBJECT
car1 = Car("Toyota", "Corolla")
print(car1.describe())
