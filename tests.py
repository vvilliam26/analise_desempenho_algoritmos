import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import pickle

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
clf = KNN(v=15, k=3)

# from busca_em_largura import BFS
# g = BFS(clf.graph)
# g.addEdge(0, 2) 
# g.addEdge(0, 3) 
# g.addEdge(0, 4) 
# g.addEdge(1, 2) 
# g.addEdge(1, 4) 
# g.addEdge(2, 4)
# g.addEdge(3, 4) 
# g.addEdge(3, 5) 
# g.addEdge(4, 5) 
# g.addEdge(5, 1)  
# print(g.bfs(5, 1))

# print(clf.graph)
from a_estrela import A_ESTRELA
a_s = A_ESTRELA(clf.v, clf.graph, grafo_vertices= clf.lista_vertices)
a_s.a_estrela(5, 1)

# a_file = open("./graphs/graph.pkl", "wb")
# pickle.dump(clf, a_file)
# a_file.close()

# leitura = open("./graphs/graph.pkl", "rb")
# bunda = pickle.load(leitura)
# print(bunda.k, bunda.v)

