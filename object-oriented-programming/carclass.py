class Car:

    def __init__(self, efficiency):
        self.efficiency = efficiency
        self.fuel = 0.0

    def add_gas(self, amount):
        self.fuel += amount

    def drive(self, miles):
        gallons = float(miles)/self.efficiency
        diff = self.fuel - gallons

        if diff < 0:
            return False
        else:
            self.fuel -= gallons
            return True

    def get_gas_level(self):
        return self.fuel


Jallopy = Car(50)

Jallopy.add_gas(30)

print Jallopy.get_gas_level()

print Jallopy.drive(1500)

print Jallopy.get_gas_level()
