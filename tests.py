from igraph import *
import pickle
import random
from a_estrela import A_ESTRELA
from a_default import A_DEF
from best1st import Best1st
from busca_em_largura import BFS
from dfs import DFS





#funcao que desenha o grafo, desenha tambem o caminho caso haja
def desenha_grafo(grafo, lyt, tamanho, path = None):
	g = Graph(directed = False)

	g.add_vertices(grafo.v)
	for vertice in grafo.lista_arestas:
		for i in range(len(vertice) - 1):
			g.add_edges([(vertice[0], vertice[i+1])])

	g.vs["color"] = "blue" #define cor dos vertices nao percorridos
	g.vs["label_size"] = 9 #tamanho das labels numericas

	#destacar path
	if(path != None):
		edges = g.es.select(_within=path)
		for i in path:
			g.vs[i]["color"] = "red"
			g.vs[i]["label"] = i
		for edge in edges:
			edge["color"] = "red"


	# labels = range(grafo.v)
	plot(g, "./grafos/imagens/imagem.png" ,vertex_size = tamanho)
	return g


#carrega o grafo, um grafo diferente para cada combinacao de valores de k e v
leitura = open("./grafos/graph_10000_7.pkl", "rb")
clf = pickle.load(leitura)

import timeit
from timeit import default_timer as timer

mediaAS=0
mediaAD=0
mediab1=0
mediabfs=0
mediadfs=0

distAD = 0
distAS = 0
distDFS = 0
distB1st = 0
distBFS = 0
numDeTestes= 20
contador = numDeTestes
while(contador>0):
	#randomiza os pontos de start e end dentro do numero de vertices
	start = random.randint(1, clf.v-1)
	end = random.randint(1, clf.v-1)

	path = list()#o path aqui so vai servir pra ver se
	#existe caminho entre o start e end gerados aleatoriamente

	#O bloco a seguir roda os testes e soma seu tempo de execucao
	#(somente se houver um caminho valido)

	# As funcoes retornam none quando nao ha caminho, entao as distancia so serao calculadas
	#quando ha 
	
	#Testa A*
	a_s = A_ESTRELA(clf)
	startT = timer()
	distanciaAS = a_s.a_estrela(start, end, path)
	endT = timer()

	if(distanciaAS!=None):
		distAS += distanciaAS
	if(path != None):
		mediaAS+=endT-startT


	#Testa A
	a_d = A_DEF(clf)

	startT = timer()
	distanciaAD = a_d.algoA(start, end)
	endT = timer()

	if(distanciaAD!=None):
		distAD += distanciaAD
	
	if(path != None):
		mediaAD+=endT-startT


	#Testa best1st
	bestfs = Best1st(clf)

	startT = timer()
	distanciaB1st = bestfs.bestFirstSearch(start, end)
	endT = timer()

	if(distanciaB1st!=None):
		distB1st += distanciaB1st

	if(path != None):
		mediab1+=endT-startT


	#Testa BFS
	breadthfs = BFS(clf)
	startT = timer()
	distanciaBFS = breadthfs.bfs(start, end)
	endT = timer()

	if(distanciaBFS!=None):
		distBFS += distanciaBFS

	if(path != None):
		mediabfs+=endT-startT

	#Testa DFS
	depthfs = DFS(clf)
	startT = timer()
	distanciaDFS = depthfs.DFS(start, end)
	endT = timer()

	if(distanciaDFS!=None):
		distDFS += distanciaDFS

	if(path != None):
		mediadfs+=endT-startT

	#Decrementa contador caso haja um caminho
	if(path != None):
		contador-=1

print("Tempo medio DFS: %s" %(mediadfs/numDeTestes*1000))
print("Distancia DFS: %s" %(distDFS/numDeTestes))
print()

print("Tempo medio A: %s " %(mediaAD/numDeTestes*1000))
print("Distancia A: %s" %(distAD/numDeTestes))
print()

print("Tempo medio A*: %s " %(mediaAS/numDeTestes*1000))
print("Distancia A*: %s" %(distAS/numDeTestes))
print()

print("Tempo medio Best1st: %s " %(mediab1/numDeTestes*1000))
print("Distancia B1st: %s" %(distB1st/numDeTestes))
print()

print("Tempo medio BFS: %s " %(mediabfs/numDeTestes*1000))
print("Distancia BFS: %s" %(distBFS/numDeTestes))
print()


print()
print()