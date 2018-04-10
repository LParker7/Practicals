from prac_07.guitar import Guitar

print("My Guitars!")
guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print("{} ({}) : ${} added.".format(name, year, cost))
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
