from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    taxi = None
    total_cost = 0
    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            taxi = choose_taxi(taxis)
        elif choice == "d":
            if taxi:
                trip_cost = drive_taxi(taxi)
                total_cost += trip_cost
        else:
            print("Invalid Option")

        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
    index = int(input("Choose taxi: "))
    return taxis[index]


def drive_taxi(taxi):
    distance = int(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)
    print("Your {} trip cost you ${:.2f}".format(taxi.name, taxi.get_fare()))
    return taxi.get_fare()


main()
