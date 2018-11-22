from numpy import random


class Animal(object):

    def __init__(self, maturity, birth_rate, death_rate):
        self.maturity = maturity
        self.birth_rate = birth_rate
        self.death_rate = death_rate

        self.is_alive = True  # Attribute, set initial value within the constructor
        self.age = 0

    def age_one_year(self):  # Method
        if self.is_alive:
            self.age += 1
            self.is_alive = random.uniform(0, 1) > self.death_rate

    def give_birth(self):
        children = []
        if self.is_alive and (self.age >= self.maturity):
            if random.uniform(0, 1) <= self.birth_rate:
                children = [Animal(self.maturity, self.birth_rate, self.death_rate)]
        return children