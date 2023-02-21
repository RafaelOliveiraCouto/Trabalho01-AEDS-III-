from typing import List

class Graph:
    def __init__(self, vertices: int = 0, arestas: int = 0, ListaDe_Adjacencia: list[list[int]] = [], ListaDe_Vertices: list[list[tuple, str, int]] = [], list_aux: list[int] = [])-> None:
        self.vertices = vertices
        self.arestas = arestas
        self.ListaDe_Adjacencia = ListaDe_Adjacencia
        self.ListaDe_Vertices = ListaDe_Vertices
        self.list_aux = list_aux
        if(ListaDe_Vertices == []):
            for i in range(self.vertices):
                self.ListaDe_Vertices.append([])
        if (ListaDe_Adjacencia == []):
            for i in range(self.vertices):
                self.ListaDe_Adjacencia.append([])


    def read_file(self, file_name):
        list_list = []
        linha = 0
        with open(file_name, "r") as file:
            for line in file:
                aux = line.split("\n")
                list_list.append(aux)
                contador = len(aux[0])
                for coluna in range(contador):
                    self.vertices += 1
                    self.ListaDe_Vertices.append([(linha, coluna), line[coluna], self.vertices])
                linha += 1
        self.ListaDe_Adjacencia = [[] for i in range(self.vertices)]
        for k in range(0, len(list_list)):
            String = list_list[k][0]
            self.list_aux.append(String)


    def AuxAresta(self, x, y):
        for i in range(0, len(self.ListaDe_Vertices)):
            if(self.ListaDe_Vertices[i][0] == (x, y)):
                return self.ListaDe_Vertices[i][2]
    def add_Arestas(self):
        aux = len(self.list_aux[0]) -1
        for i in range(0, len(self.list_aux)):
            for j in range(0, len(self.list_aux[i])):
                if (self.list_aux[i][j] != '#' and (i - 1) >= 0 and self.list_aux[i - 1][j] != '#'):    # Verifica o de cima para ver se pode ter uma ligação nele
                    u = self.AuxAresta(i, j)
                    v = self.AuxAresta((i - 1), j)
                    self.add_directed_edge(u, v)

                if(self.list_aux[i][j] != '#' and (i + 1) <= len(self.list_aux) and self.list_aux[i+1][j] != '#'):   # Verifica o de baixo para ver se pode ter uma ligação nele
                    u = self.AuxAresta(i, j)
                    v = self.AuxAresta((i + 1), j)
                    self.add_directed_edge(u, v)

                if(self.list_aux[i][j] != '#' and (j - 1) >= 0 and self.list_aux[i][j - 1] != '#'): # Verifica a esquerda para ver se pode ter uma ligação nele
                    u = self.AuxAresta(i, j)
                    v = self.AuxAresta(i, (j - 1))
                    self.add_directed_edge(u, v)

                if(self.list_aux[i][j] != '#' and (j + 1) <= aux and self.list_aux[i][j+1] != '#'): # Verifica a direita para ver se pode ter uma ligação nele
                    u = self.AuxAresta(i, j)
                    v = self.AuxAresta(i, (j + 1))
                    self.add_directed_edge(u, v)


    # Adicionar uma aresta direcionada || u = Nó de saida e v = Nó de entrada
    def add_directed_edge(self, u: int, v: int):
        if(u >= 0 and u < self.vertices and v >= 0 and v < self.vertices):
            self.ListaDe_Adjacencia[u].append(v)
            self.arestas += 1
            return
        print(f"Node u={u} or v={v} is out of allowed range (0, {self.arestas - 1})")


    def Ordenar_ListaDe_Adjacencia(self):
        for i in range(len(self.ListaDe_Adjacencia)):
            self.ListaDe_Adjacencia[i].sort()


    def dfsAuxiliar(self, u, descoberto):
        for v in self.ListaDe_Adjacencia[u]:
            if(descoberto[v] == 0):
                return v
        return -1
    def dfs(self):
        for u in range(0, len(self.ListaDe_Vertices)):
            if(self.ListaDe_Vertices[u][1] == 'S'):
                s = self.ListaDe_Vertices[u][2]
        descoberto = []
        for u in range(0, self.vertices):     # Criar uma lista descoberto zerado
            descoberto.append(0)                # Tem outro modo de se fazer isso: descoberto = [0 for _ in range(self.node_count)
        S = [s]
        R = [s]
        descoberto[s] = 1
        while(len(S) != 0):
            u = S[-1]
            v = self.dfsAuxiliar(u, descoberto)
            if(v != -1):
                S.append(v)
                R.append(v)
                descoberto[v] = 1
            else:
                S.pop()


        list_tupla = []
        for i in range(len(R)):
            v = R[i] -1
            coord = self.ListaDe_Vertices[v][0]
            tupla = (coord)
            list_tupla.append(tupla)


        return  R