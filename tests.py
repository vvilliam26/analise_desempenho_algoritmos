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


leitura = open("./grafos/graph_10000_7.pkl", "rb")
clf = pickle.load(leitura)


import timeit

from timeit import default_timer as timer



from a_estrela import A_ESTRELA

mediaAS=0
mediaAD=0
mediab1=0
mediabfs=0
mediadfs=0
i = 10
while(i>0):
	start = random.randint(1, clf.v-1)
	end = random.randint(1, clf.v-1)
	a_s = A_ESTRELA(clf)
	startT = timer()
	path = a_s.a_estrela(end = end, start = start, n = clf.v)
	endT = timer()
	if(path != None):
		mediaAS+=endT-startT


	from a_default import A_DEF
	a_d = A_DEF(clf)
	startT = timer()
	a_d.bestFirstSearch(start, end, clf.v)
	endT = timer()
	if(path != None):
		mediaAD+=endT-startT


	from best1st import Best1st
	bestfs = Best1st(clf)
	startT = timer()
	bestfs.bestFirstSearch(start, end, clf.v)
	endT = timer()
	if(path != None):
		mediab1+=endT-startT


	from busca_em_largura import BFS
	breadthfs = BFS(clf)
	startT = timer()
	breadthfs.bfs(start, end)
	endT = timer()
	if(path != None):
		mediabfs+=endT-startT

	from dfs import DFS
	depthfs = DFS(clf)
	startT = timer()
	depthfs.DFS(start, end)
	endT = timer()
	if(path != None):
		mediadfs+=endT-startT
	if(path != None):
		i-=1

print(mediadfs*100)
print(mediaAD*100)
print(mediaAS*100)
print(mediab1*100)
print(mediabfs*100)







print()
print()