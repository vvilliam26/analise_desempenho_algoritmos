import numpy as np

# def distancia_euclidiana(x1, x2):
#     distance = 0.0
#     for i in range(len(x1) - 1):
#         distance += (x1[i] - x2[i])**2
#     return np.sqrt(distance)


dataset = [[2.7810836,2.550537003],
	[1.465489372,2.362125076],
	[3.396561688,4.400293529],
	[1.38807019,1.850220317],
	[3.06407232,3.005305973],
	[7.627531214,2.759262235],
	[5.332441248,2.088626775],
	[6.922596716,1.77106367],
	[8.675418651,-0.242068655],
	[7.673756466,3.508563011]]

from knn import KNN
v=100
clf = KNN(k=3, v=100)
# clf.set_arestas()
# clf.grafo()

from busca_em_largura import BFS
# bfs = BFS(clf.lista_arestas)

# row0 = dataset[0]
# for row in dataset:
#     distance = euclidean_distance(row0, row)
#     print(distance)



# from knn import KNN
# clf = KNN(v=5,k=2)
# print(clf.gerar_coordenadas())

from dfs import DFS
test = DFS(clf)
test.DFS(67, 54)

from best1st import Best1st
buscaInformada = Best1st(clf)
buscaInformada.bestFirstSearch(67, 54, v)



