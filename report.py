import numpy as np
from knn import KNN
from busca_em_largura import BFS
from dfs import DFS
#from a_star import

vs = list()
vs.append(500)
vs.append(5000)
vs.append(10000)

ks = list()
ks.append(3)
ks.append(5)
ks.append(7)

for k in ks:
    for v in vs:
        clf = KNN(k, v)
        test = DFS(clf.lista_arestas)
        test.DFS(start, end)
    