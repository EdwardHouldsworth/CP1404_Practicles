from prac_08.unreliable_car import UnreliableCar

bad_car = UnreliableCar("BadCar",100,40)
print(bad_car)
for x in range(0,10):
    bad_car.drive(10)
    print(bad_car)
