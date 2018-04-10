class Guitar:
    CURRENT_YEAR = 2018
    VINTAGE_AGE = 50

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= self.VINTAGE_AGE
