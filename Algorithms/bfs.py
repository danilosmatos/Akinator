arvoreTeste = {
        '1':  ['2', '3', '4'],
    '2':  ['1', '5', '6', '7'],
    '3':  ['1', '8', '9'],
    '4':  ['1', '10', '11', '12'],
    '5':  ['2', '13', '14'],
    '6':  ['2', '15'],
    '7':  ['2', '16', '17'],
    '8':  ['3', '18', '19'],
    '9':  ['3', '20'],
    '10': ['4', '21', '22'],
    '11': ['4', '23'],
    '12': ['4', '24', '25'],
    '13': ['5'],
    '14': ['5'],
    '15': ['6'],
    '16': ['7'],
    '17': ['7'],
    '18': ['8'],
    '19': ['8'],
    '20': ['9'],
    '21': ['10'],
    '22': ['10'],
    '23': ['11'],
    '24': ['12'],
    '25': ['12'],

}

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
def caminho (grafo, origem, destino ):
    pais = bfs(grafo, origem)
    
    return menorCaminho(pais, origem, destino)


print(caminho(arvoreTeste, '1', '25'))
print(caminho(arvoreTeste, '2', '25'))
print(caminho(arvoreTeste, '3', '13'))
print(caminho(arvoreTeste, '4', '13'))


