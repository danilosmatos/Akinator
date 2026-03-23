from collections import deque

def bfs(raiz):
    visitados = []
    queue = deque([raiz])

    while queue:
        no = queue.popleft()

        if no.pergunta:
            visitados.append(no.pergunta)

        else:
            visitados.append(no.resposta)

        if no.yes:
            queue.append(no.yes)
        if no.no:
            queue.append(no.no)
    return visitados




def menorCaminho(pais, origem, destino):
    if destino not in pais and destino != origem:
        return []
    
    trilha = [destino]
    noAtual = destino

    while noAtual != origem:
        noAtual = pais[noAtual]
        trilha.append(noAtual)
    trilha.reverse()
    return trilha


if __name__ == '__main__':
    from tree import ArvoreDecisao

    arvore = ArvoreDecisao()

    print('---- Ordem das visitas ----')

    ordem = bfs(arvore.raiz)

    for i, no in enumerate(ordem):
        print(f'{i+1}. {no}')
