#Encapsulation
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance()) 

#Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."
    
    def stop_engine(self):
        return "Car engine stopped."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."
    
    def stop_engine(self):
        return "Motorcycle engine stopped."

car = Car()
bike = Motorcycle()

print(car.start_engine())  
print(bike.start_engine())  

#Composition
class Engine:
    def start(self):
        return "Engine started."

    def stop(self):
        return "Engine stopped."

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_engine(self):
        return self.engine.start()
    
    def stop_engine(self):
        return self.engine.stop()

car = Car()
print(car.start_engine()) 
