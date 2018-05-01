from prac_08.silver_service_taxi import SilverServiceTaxi

car = SilverServiceTaxi('SST', 100, 2)
print(car)
car.drive(18)
print("Total fare cost = ${:.2f}".format(car.get_fare()))
