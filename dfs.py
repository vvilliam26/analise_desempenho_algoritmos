from collections import defaultdict
from math import sqrt
from sys import setrecursionlimit

setrecursionlimit(500000)#Nao fazer isso pode ocasionar erro no algoritmo

def distancia_euclidiana(x1, x2):
    sum = 0
    for i in range (0,1):
        sum+=(x1[i]+x2[i])**2
    return sqrt(sum)
 
class DFS:
    # Construtor da classe, so pra receber o grafo msm
    def __init__(self, grafo_knn):
        self.set_grafo(grafo_knn)


    def set_grafo(self, grafo_knn):
        self.grafo = grafo_knn
 
 
    # Parte recursiva do algoritmo
    def DFSUtil(self, v, end, visited, path, prev):
 
        # Marca o no atual como visitado para nao ser visitado de novo
        visited.add(v)

        #Soma a distancia do no atual ao anterior
        #Se não for o caminho certo, subtrai no final
        if(prev!=None):
            self.dist+=distancia_euclidiana(self.grafo.lista_vertices[prev], 
            self.grafo.lista_vertices[v])
        
        #Se v for o end, encerra dps de botar no path
        if(v == end):
            path.append(v)
            return True
 
        # Percorre recursivamente, indo sempre em profundidade nos nos
        for neighbour in self.grafo.graph[v]:
            if neighbour not in visited:
                prev = v
                #Se o branch atual for um caminho, bota todos nos na path
                #Sim, o path fica ao contrario, mas na hora de printar eu uso reverse
                if self.DFSUtil(neighbour, end, visited, path, prev) == True:
                    path.append(v)
                    return True

        #Caso nao seja o primeiro nó e não seja o caminho certo, 
        #subtrai a distancia somada anteriormente
        if(self.dist>0):
            self.dist -= distancia_euclidiana(self.grafo.lista_vertices[prev], self.grafo.lista_vertices[v])

        return False
 
    # Função que inicializa as vars e listas da funcao recursiva
    def DFS(self, start, end):
 
        # Cria um set de nos visitados, set facilita a verificação
        visited = set()

        #List to store path
        path = list()
        self.dist = 0.0

        #No anterior, feito pra calcular a distancia
        prev = None

        # Chama a func recursiva e retorna o path
        if(self.DFSUtil(start,end, visited, path, prev)==True):
            path.reverse()
            return self.dist

        