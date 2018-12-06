from numpy.random import randint


class Genes(object):

    def __init__(self):
        self.genes = None

    def deadly_mutations(self, year):
        return sum(self.genes[:year])

    def __len__(self):
        return len(self.genes)

    def clone(self):
        genes = Genes()
        genes.genes = self.genes
        return genes

    def clone_with_mutations(self, mutations):
        genes = self.clone()
        genes.mutate(mutations)
        return genes

    def mutate(self, mutations):
        flip_genes(self, mutations)

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
        flip_genes(genes, initial_mutations)
        return genes


def insert_deadly_mutations(genes, mutations):
    """
    Insert number of mutations into genes vector

    :param genes: list of 0 and 1
    :param mutations: integer
    :return: None
    """
    positions = randint(0, len(genes), mutations)
    for p in positions:
        genes[p] = 1


def flip_genes(genes, num_flips):
    """
    Flips certain number of genes given by num_flips.
    :param genes: list of 0 and 1
    :param num_flips: integer
    :return:
    """
    positions = randint(0, len(genes), num_flips)
    for p in positions:
        genes.flip(p)
