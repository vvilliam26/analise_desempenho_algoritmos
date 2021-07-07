from igraph import *
import pickle
import random

def desenha_grafo(grafo, lyt, tamanho, path = None):
	g = Graph(directed = False)

	g.add_vertices(grafo.v)
	for vertice in grafo.lista_arestas:
		for i in range(len(vertice) - 1):
			g.add_edges([(vertice[0], vertice[i+1])])

	g.vs["color"] = "blue"
	g.vs["label_size"] = 9

	if(path != None):
		edges = g.es.select(_within=path)
		for i in path:
			g.vs[i]["color"] = "red"
		for edge in edges:
			edge["color"] = "red"


	labels = range(grafo.v)
	plot(g, "./grafos/imagens/imagem.png" ,vertex_size = tamanho, vertex_label = labels)
	return g

# dataset = [[2.7810836,2.550537003],
# 	[1.465489372,2.362125076],
# 	[3.396561688,4.400293529],
# 	[1.38807019,1.850220317],
# 	[3.06407232,3.005305973],
# 	[7.627531214,2.759262235],
# 	[5.332441248,2.088626775],
# 	[6.922596716,1.77106367],
# 	[8.675418651,-0.242068655],
# 	[7.673756466,3.508563011]]

#import igraph
#from knn import KNN
#clf = KNN(v=500, k=7)

leitura = open("./grafos/graph_5000_7.pkl", "rb")
clf = pickle.load(leitura)

# print(clf.graph)

import timeit

from timeit import default_timer as timer



from a_estrela import A_ESTRELA

mediaAS=0
mediaAD=0
mediab1=0
mediabfs=0
mediadfs=0
for i in range(1, 1000):
	start = random.randint(1, clf.v-1)
	end = random.randint(1, clf.v-1)
	a_s = A_ESTRELA(clf)
	startT = timer()
	a_s.a_estrela(end = end, start = start, n = clf.v)
	endT = timer()
	mediaAS+=endT-startT
	# if(path != None):
	# 	desenha_grafo(clf, "drl", 10, path)

	from a_default import A_DEF
	a_d = A_DEF(clf)
	startT = timer()
	a_d.bestFirstSearch(start, end, clf.v)
	endT = timer()
	mediaAD+=endT-startT
	# if(path != None):
	# 	desenha_grafo(clf, "drl", 10, path)

	from best1st import Best1st
	bestfs = Best1st(clf)
	startT = timer()
	bestfs.bestFirstSearch(start, end, clf.v)
	endT = timer()
	mediab1+=endT-startT
	# if(path != None):
	# 	desenha_grafo(clf, "drl", 10, path)

	from busca_em_largura import BFS
	breadthfs = BFS(clf)
	startT = timer()
	breadthfs.bfs(start, end)
	endT = timer()
	mediabfs+=endT-startT# if(path != None):
	# 	desenha_grafo(clf, "drl", 10, path)

	from dfs import DFS
	depthfs = DFS(clf)
	startT = timer()
	depthfs.DFS(start, end)
	endT = timer()
	mediadfs+=endT-startT
# if(path != None):
# 	desenha_grafo(clf, "drl", 10, path)
print(mediadfs)
print(mediaAD)
print(mediaAS)
print(mediab1)
print(mediabfs)



#a_file = open("./grafos/graph_5000_3.pkl", "wb")
#pickle.dump(clf, a_file)
#a_file.close()


# print(path)
#if(path != None):
desenha_grafo(clf, "drl", 10)
print()
print()