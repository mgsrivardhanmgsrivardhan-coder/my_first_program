class Student:
    def __init__(self, name, roll): # Constructor + self
        self.name = name
        self.roll = roll
    
    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

s1 = Student("Aman", 101)
s1.show()
