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

    def flip(self, position):
        if self.genes[position] == 1:
            self.genes[position] = 0
        elif self.genes[position] == 0:
            self.genes[position] = 1
        else:
            raise ValueError('Genes value on position is %s' % self.genes[position])

    @classmethod
    def create(cls, length, initial_mutations):
        genes = Genes()
        genes.genes = [0] * length
        insert_deadly_mutations(genes.genes, initial_mutations)
        return genes


def insert_deadly_mutations(genes, mutations):
    positions = randint(0, len(genes), mutations)
    for p in positions:
        genes[p] = 1


def flip_genes(genes, num_flips):
    positions = randint(0, len(genes), num_flips)
    for p in positions:
        genes.flip(p)
