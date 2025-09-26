class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """InItialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
        self.fuel_tank = 70
        self.fuel_level = 0

    def fill_tank(self):
        """Fill the car's fuel tank."""
        self.fuel_level = self.fuel_tank
        print("The fuel tank is now full.")

    def drive(self):
        """Simulate driving the car."""
        if self.fuel_level > 0:
            print("The car is now driving.")
            self.fuel_level -= 10
        else:
            print("The fuel tank is empty. Please fill the tank.") 



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75  # in kWh
        self.battery_level = 0  # in percentage

    def charge_battery(self):
        """Charge the car's battery."""
        self.battery_level = 100
        print("The battery is now fully charged.")

    def drive(self):
        """Simulate driving the electric car."""
        if self.battery_level > 0:
            print("The electric car is now driving.")
            self.battery_level -= 10
        else:
            print("The battery is empty. Please charge the battery.")
    
    def fill_tank(self):
        """Electric cars do not have fuel tanks."""
        print("This car doesn't have a fuel tank!")



my_care = Car('audi', 'a4', 2019)
print(f"My car is a {my_care.year} {my_care.make} {my_care.model}.")


my_electric_car = ElectricCar('tesla', 'model s', 2020)
print(f"My electric car is a {my_electric_car.year} {my_electric_car.make} {my_electric_car.model}.")



my_care.fill_tank()
my_care.drive()


my_electric_car.charge_battery()
my_electric_car.drive()
