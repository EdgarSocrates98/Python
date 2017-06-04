"""
ANTES DE TESTAR LEIA O ARQUIVO TXT!
=======================================================================
Importando a Lib numpy, pois através dela carregarei os dados do grafo;

Carregando os dados da edges.dat e os convertendo para List

"""

import numpy as ny


grafoss = ny.genfromtxt('edges.dat', delimiter = '')
grafoss = grafoss.tolist()

"""
Utilizei deste metodo para ter certeza quantas vertices teria o grafo,
após conhecer a quantidade de vertices que no caso vão 0 a 99 de  adicionei
o método neste comentario.

print(grafo)

"""
vertices = 100

"""
Criando a lista de aproximação e sua ordenação.
"""

lista_aproximacao = [[] for vertice in range(0, vertices)]

for ver in range(0, vertices):
    for grafo in grafoss:

        if ver in grafo:
            id = grafo.index(ver)

            if id != 0:
                lista_aproximacao[ver].append(grafo[0])
            else:
                lista_aproximacao[ver].append(grafo[1])


for aretas in range(0, len(lista_aproximacao)):
    lista_aproximacao[aretas].sort()


"""
Aplicando um método de busca em amplitude, após o algoritmo realizar toda sua
travessia pelo grafo e chegar no ultimo vertice ele retornará a raiz do grafo
(posição inicial), assim imprimindo no terminal o resultado de sua busca.
"""
gr = [[] for i in range(0, vertices)]

for vertice in range(0, vertices):
    distanciamento = [float('inf') for i in range(0, vertices)]

    distanciamento[vertice] = 0

    lista = []
    lista.append(vertice)

    while len(lista) != 0:

        cl = lista.pop(0)

        for ver in lista_aproximacao[int(cl)]:

            if distanciamento[int(ver)] == float('inf'):
                distanciamento[int(ver)] = distanciamento[int(cl)]+1
                lista.append(ver)

    gr[vertice] = 1/(sum(distanciamento))


ordem = [[] for i in range(0, vertices)]

for i in range(0, vertices):

    num_final = gr.index(max(gr))
    ordem[i] = num_final
    gr[num_final] = 0

print(ordem)
