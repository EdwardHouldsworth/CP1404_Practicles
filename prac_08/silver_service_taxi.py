from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness = 0.0):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.50

    def __str__(self):
        return super().__str__() + "plus flagfall of {}".format(self.flagfall)

    def get_fare(self):
        return super().get_fare() + self.flagfall