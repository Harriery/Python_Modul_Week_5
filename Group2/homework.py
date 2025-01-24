class Vehicle:
    species = "interesting_autos"
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} is a {self.model} model car made in {self.year}."

    def value(self, price):
        return f"{self.make} and {self.model} car is worth {price} dollars."

    def speak(self, sound):
        return f"{self.make} says {sound}."


class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive  # Off-road vehicle-specific feature

    def __str__(self):
        return super().__str__() + f" It has four-wheel drive: {self.four_wheel_drive}."


class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed  # Sports car-specific feature

    def __str__(self):
        return super().__str__() + f" Its max speed is {self.max_speed} km/h."


# Creating instances of each class
clio = OffRoadVehicle("Clio", "sedan", 2010, True)
egea = SportsCar("Egea", "sedan", 2015, 220)
toyota = OffRoadVehicle("Toyota", "Land Cruiser", 2023, True)
mitsubushi = SportsCar("Mitsubishi", "Eclipse", 2008, 250)

# Displaying information
print(clio)
print(clio.value(5000))

print(egea)
print(egea.value(15000))

print(toyota)
print(mitsubushi.value(10000))

# Checking the type and instance
print(type(clio))
print(isinstance(mitsubushi, Vehicle))