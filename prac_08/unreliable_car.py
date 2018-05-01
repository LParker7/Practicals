"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name='Car', fuel=0, reliability=100):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance_of_success = randint(0, 100)
        if self.reliability > chance_of_success:
            return super().drive(distance)
        else:
            return 0
