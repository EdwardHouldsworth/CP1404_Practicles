"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("Limo fuel = {self.fuel}".format(self=limo))
    limo.drive(115)
    print(limo)


main()
