import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
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
# clf = KNN(v=10, k=3, dataset = dataset)
# clf.set_arestas()
# clf.grafo()

from busca_em_largura import BFS
g = BFS()
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(0, 4) 
g.addEdge(1, 2) 
g.addEdge(1, 4) 
g.addEdge(2, 4)
g.addEdge(3, 4) 
g.addEdge(3, 5) 
g.addEdge(4, 5) 
g.addEdge(5, 1)  
print(g.bfs(0, 1))


# plt.plot(dataset, 'o', color = 'black')
# plt.show()

# from knn import KNN
# clf = KNN(v=5,k=2)
# print(clf.gerar_coordenadas())

#from dfs import DFS
#test = DFS(clf.lista_arestas)
#test.DFS(0, 2)



