from tree import Tree
import random

arvoreTeste = Tree()
valores = random.sample(range(1, 100), 10)
print(f'Valores da Árvore: {valores}')
for v in valores:
    arvoreTeste.inserir(v)

grafo = arvoreTeste.para_grafo()
print(f'Grafo da Árvore: {grafo}')

def bfs(grafo, no1):
    visitados = []
    queue = [no1]
    pais = {}
    while queue:
        noAtual = queue.pop(0)
        visitados.append(noAtual)
        for vizinho in grafo[noAtual]:
            if vizinho not in visitados:
                queue.append(vizinho)
                pais[vizinho] = noAtual
    return pais

def menorCaminho(pais, origem, destino):
    trilha = [destino]
    noAtual = destino
    while noAtual != origem:
        noAtual = pais[noAtual]
        trilha.append(noAtual)
    trilha.reverse()
    return trilha

def caminho(grafo, origem, destino):
    pais = bfs(grafo, origem)
    return menorCaminho(pais, origem, destino)

nos = list(grafo.keys())
raiz = str(arvoreTeste.raiz.valor)

print(f'\nCaminho de {raiz} até {nos[-1]}:')
print(caminho(grafo, raiz, nos[-1]))

print(f'\nCaminho de {raiz} até {nos[-2]}:')
print(caminho(grafo, raiz, nos[-2]))