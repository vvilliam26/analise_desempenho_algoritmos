from math import sqrt
from collections import Counter
import random
from collections import defaultdict

#Distancia euclidiana de um elemento em relacao aos elementos testes
def distancia_euclidiana(x1, x2):
    distancia = 0.0
    for i in range(len(x1)):
        distancia += (x1[i] - x2[i])**2
    return sqrt(distancia)

#Acha os vizinhos do item e retorna [x, y, index]
def get_vizinhos(k, coordenada_teste, coordenadas):
    distancias = list()
    index = 0
    for coordenada in coordenadas:
        dist = distancia_euclidiana(coordenada_teste, coordenada)
        distancias.append((coordenada, dist, index))
        index += 1
    distancias.sort(key=lambda tup: tup[1])

    vizinhos = list()
    for i in range(k + 1):
        vizinhos.append([distancias[i][0], distancias[i][2]])
    return vizinhos


class KNN:

    def __init__(self, k, v, dataset):
        # self.k = k
        # self.v = v
            #linha abaixo para inserir uma datasheet
        self.lista_vertices = dataset
        # self.lista_vertices = self.gerar_coordenadas(v)
        self.set_arestas(k)
        self.set_grafo()

    def get_viz(self, dt):
        print(get_vizinhos(self.k, dt[0], dt))

    #gerando V elementos com coordenadas x e y com random()
    def gerar_coordenadas(self, v):
        lista_vertices = []
        for i in range(v):
            coord = [random.random()*v, random.random()*v]
            lista_vertices.append(coord)
        self.lista_vertices = lista_vertices

    #Acha os vizinhos do item e retorna uma lista na qual a cabeça eh o index da coordenada no array de vertices
    #e a calda sao os elementos os quais este estah conectado (arestas)
    def set_arestas(self, k):
        lista_arestas = list()
        for vertice in self.lista_vertices:
            vizinhos = get_vizinhos(k, vertice, self.lista_vertices)
            vizinhos_index = list()
            for i in range(k + 1):
                vizinhos_index.append(vizinhos[i][1])
            lista_arestas.append(vizinhos_index)
        self.lista_arestas = lista_arestas
        # print(lista_arestas)
        
    # def _predict(self, x):
    #     distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

    #     k_indexes = np.argsort(distances)[:self.k]
    #     k_nearest_labels = [self.y_train[i] for i in k_indexes]

    #     most_commom = Counter(k_nearest_labels).most_common(1)
    #     return most_commom[0][0]

    #Printa o grafo por lista de adjacência e em ordem crescente de distancia
    # def grafo(self):
    #     for aresta in self.lista_arestas:
    #         print(f'{aresta[0]}:', end='    ')
    #         calda = aresta[1:]
    #         print(calda)
    #         print('')

    def set_grafo(self):
        self.graph = defaultdict(list)
        
        for vertice in self.lista_arestas:
            for u in range(len(vertice)-1):
                self.graph[vertice[0]].append(vertice[u+1])
        print (self.graph)
    
