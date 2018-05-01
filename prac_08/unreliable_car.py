"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name='Car', fuel='0', reliability='100'):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.odometer = 0

    def drive(self, distance):
        chance_of_success = randint(0,100)
        if self.reliability > chance_of_success:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance

