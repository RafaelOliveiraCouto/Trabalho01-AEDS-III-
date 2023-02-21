from Graph import Graph
import time


i = 0
while(i != 1):
    print('\nOpções: ')
    print('toy.txt')
    print('maze3.txt')
    print('maze10.txt')
    print('maze20.txt')
    print('maze30.txt')
    print('maze40.txt')
    print('maze50.txt')
    escolha = input('Digite qual arquivo quer abrir: ')
    g1 = Graph(ListaDe_Adjacencia=[], ListaDe_Vertices=[], list_aux=[])
    g1.read_file("Datasets/"+escolha)
    g1.add_Arestas()
    start_time = time.time()
    print("DFS FROM GRAPH 1:", g1.dfs())
    print("Elapsed time", time.time() - start_time)

    i = int(input('Digite 1 para sair || Digite qualquer numero para continuar: '))
