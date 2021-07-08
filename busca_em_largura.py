
class BFS:

    #constroi a função que ira criar a lista 
    def __init__(self, grafo_knn): 
        self.graph = grafo_knn.graph

    #recebe start e target
    def bfs(self, start, end):

        visited = []

        queue = [[start]]

        if start== end:
            return "Start = Target"

        while queue:

            caminhos = queue.pop(0)


            vertice = caminhos[-1]
            if vertice not in visited:
                vizinhos = self.graph[vertice]
                for vizinho in vizinhos:
                    novo_caminho = list(caminhos)
                    novo_caminho.append(vizinho)
                    queue.append(novo_caminho)

                    if vizinho == end:
                        print("Caminho BFS: %s" %(novo_caminho))

                        #return distTotal
                visited.append(vertice)
    

