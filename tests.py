from igraph import *
import pickle

def desenha_grafo(grafo, lyt, tamanho, path = None):
	g = Graph(directed = False)

	g.add_vertices(grafo.v)
	for vertice in grafo.lista_arestas:
		for i in range(len(vertice) - 1):
			g.add_edges([(vertice[0], vertice[i+1])])

	g.vs["color"] = "blue"

	if(path != None):
		edges = g.es.select(_within=path)
		for i in path:
			g.vs[i]["color"] = "red"
		for edge in edges:
			edge["color"] = "red"


	labels = range(grafo.v)
	plot(g, vertex_size = tamanho, vertex_label = labels)
	return g

			

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

import igraph
from knn import KNN
clf = KNN(v=50, k=7)

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
a_s = A_ESTRELA(clf)
path = a_s.a_estrela(5, 1)

# a_file = open("./grafos/graph.pkl", "wb")
# pickle.dump(clf, a_file)
# a_file.close()

# leitura = open("./grafos/graph.pkl", "rb")
# clf = pickle.load(leitura)

print(path)
desenha_grafo(clf, "drl", 20, path = path)