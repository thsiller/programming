from penna.genes import Genes



g = Genes.create(10, 2)

print(g.genes)
g = g.clone()
print(g.genes)
g = g.clone_with_mutations(4)
print(g.genes)
g.mutate(5)
print(g.genes)