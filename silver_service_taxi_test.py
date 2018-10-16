from prac_08.silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("SilverTaxi",100,2)
silver_taxi.start_fare()
silver_taxi.drive(18)
print(silver_taxi.get_fare())