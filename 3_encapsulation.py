class Bank:
    def __init__(self, balance):
        self.__balance = balance # private attribute
    
    @property
    def balance(self): # getter
        return self.__balance
    
    @balance.setter
    def balance(self, value): # setter with validation
        if value >= 0:
            self.__balance = value

b = Bank(1000)
print(b.balance)
b.balance = 500
print(b.balance)
