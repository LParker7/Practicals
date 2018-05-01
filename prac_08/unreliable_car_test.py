from prac_08.unreliable_car import UnreliableCar

car = UnreliableCar('Unreliable Car', 100, 80)
for trip in range(0,5):
    print("Distance travelled in trip {} = {}km".format(trip+1, car.drive(20)))
    print(car)
