from prac_08.taxi import Taxi

# Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
prius = Taxi("Prius 1", 100)
prius.start_fare()

# Drive the taxi 40km
prius.drive(40)

# Print the taxi's details and the current fare
print(prius)

# Restart the meter (start a new fare) and then drive the car 100km
prius.start_fare()
prius.drive(100)

# Print the details and the current fare
print(prius)