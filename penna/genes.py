from numpy.random import randint


class Genes(object):

    def __init__(self):
        self.genes = None

    def deadly_mutations(self, year):
        return sum(self.genes[:year])

    def clone(self):
        genes = Genes()
        genes.genes = self.genes
        return genes

    def clone_with_mutations(self, mutations):
        genes = self.clone()
        genes.mutate(mutations)
        return genes

    def mutate(self, mutations):
        insert_deadly_mutations(self.genes, mutations)

    @classmethod
    def create(cls, lenght, initial_mutations):
        genes = Genes()
        genes.genes = [0] * lenght
        insert_deadly_mutations(genes.genes, initial_mutations)
        return genes


def insert_deadly_mutations(genes, mutations):
    positions = randint(0, len(genes), mutations)
    for p in positions:
        genes[p] = 1