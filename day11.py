#Object oriented programming
#class and object
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is now running.")

    def stop_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is now off.")

    def describe(self):
        print(f"This car is a {self.color} {self.year} {self.make} {self.model}.")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2021, "blue")

# Using the object's methods
my_car.describe()
my_car.start_engine()
my_car.stop_engine()

#inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, color, battery_capacity):
        super().__init__(make, model, year, color)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"The battery of the {self.year} {self.make} {self.model} is now charging.")

my_electric_car = ElectricCar("Tesla", "Model S", 2022, "red", 100)

my_electric_car.describe()
my_electric_car.charge_battery()
my_electric_car.start_engine() 

#polymorphism 
def test_drive(car):
    car.describe()
    car.start_engine()
    car.stop_engine()

# Using the test_drive function with different types of cars
test_drive(my_car)
test_drive(my_electric_car)


