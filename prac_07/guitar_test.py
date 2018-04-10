from prac_07.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2012)

print(guitar1)
print(guitar2)

print("{} get_age() - Expected 96. Got {}".format(guitar1.name, guitar1.get_age()))
print("{} get_age() - Expected 6. Got {}".format(guitar2.name, guitar2.get_age()))

print("{} is_vintage() - Expected True. Got {}".format(guitar1.name, guitar1.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(guitar2.name, guitar2.is_vintage()))
