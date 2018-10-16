from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi
from prac_08.unreliable_car import UnreliableCar

taxis = []


def show_taxis():
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi.name))


def main():
    taxis.append(Taxi("Normal Taxi", 100))
    taxis.append(SilverServiceTaxi("Silver Taxi", 100, 2))
    taxis.append(UnreliableCar("Unreliable Taxi", 100, 40))

    user_bill = 0
    show_taxis()
    user_input = input("Enter a Taxi 'number' 'comma' and distance' eg. 1, 45"
                       "or Q to quit")
    while user_input.upper() != "Q":

        show_taxis()
        user_input = input("Enter a Taxi 'number' 'comma' and distance' eg. 1, 45"
                           "or Q to quit")
main()

