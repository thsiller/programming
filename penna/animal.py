from numpy import random
from penna.genes import Genes

class Animal(object):

    def __init__(self, maturity, birth_rate, deadly_mutations, mutations_per_year, genes):
        self.maturity = maturity
        self.birth_rate = birth_rate
        self.deadly_mutations = deadly_mutations
        self.mutations_per_year = mutations_per_year
        self.genes = genes

        self.is_alive = True  # Attribute, set initial value within the constructor
        self.age = 0

    def __str__(self):
        return str(self.genes.genes) + ' age: %s' % self.age

    def age_one_year(self):  # Method
        if self.is_alive:
            self.age += 1
            self.genes.mutate(self.mutations_per_year)
            self.is_alive = not (self.genes.deadly_mutations(self.age) >= self.deadly_mutations)


    @classmethod
    def create(cls, maturity, birth_rate, deadly_mutations, initial_mutations, mutations_per_year=2, genes_length=10):
        genes = Genes.create(genes_length, initial_mutations)
        animal = cls(maturity, birth_rate, deadly_mutations, mutations_per_year, genes)
        return animal


    def give_birth(self):
        children = []
        if self.is_alive and (self.age >= self.maturity):
            if random.uniform(0, 1) <= self.birth_rate:
                genes = self.genes.clone()
                child = Animal(self.maturity, self.birth_rate, self.deadly_mutations, self.mutations_per_year, genes)
                children = [child]
        return children



