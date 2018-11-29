from penna.genes import Genes



a = Genes.create(10, 2)
print('genes as is:', a.genes, id(a))
g = Genes.create(10, 2)
print('genes as is:', g.genes, id(g))
g = g.clone()
print('clone of genes: ', g.genes, id(g))
g = g.clone_with_mutations(4)
print('clone with mutations: ', g.genes)
g.mutate(5)
print('mutatations applied on the last one: ', g.genes)
g.flip(5)
print('mutatations flipped: ', g.genes)
g.flip(5)
print('mutatations flipped: ', g.genes)
g.flip(5)
print('mutatations flipped: ', g.genes)
g.flip(5)
print('mutatations flipped: ', g.genes)

