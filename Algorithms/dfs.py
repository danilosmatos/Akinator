from node import Node

def dfs(node, visitados=None):
    if visitados is None:
        visitados = []

    if node is None:
        return visitados

    valor = node.pergunta if node.pergunta else node.resposta
    visitados.append(valor)

    dfs(node.yes, visitados)
    dfs(node.no, visitados)

    return visitados
