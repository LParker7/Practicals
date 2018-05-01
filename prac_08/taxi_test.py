from prac_08.taxi import Taxi

car = Taxi('Prius 1', 100)
car.drive(40)
print(car)
print(car.get_fare())
car.start_fare()
car.drive(100)
print(car)
print(car.get_fare())