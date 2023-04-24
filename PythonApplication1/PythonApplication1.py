class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The car is starting.")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("The electric car is charging.")

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
print(my_electric_car.make)           # output: Tesla
print(my_electric_car.battery_capacity)  # output: 100
my_electric_car.start()               # output: The car is starting.
my_electric_car.charge()              # output: The electric car is charging.
