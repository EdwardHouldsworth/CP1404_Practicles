from prac_08.car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        self.reliability = reliability
        super().__init__(name, fuel)

    def drive(self, distance):
        if random.randint(0,100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        return 0