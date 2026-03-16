import random
class Nodes:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Tree:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        novo = Nodes(dado)

        if self.raiz == None:
            self.raiz = novo
            return
        atual = self.raiz
        while True:
            if dado < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = novo
                return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita
    def remover(self, valor):
        pai = None
        atual = self.raiz
        while atual and atual.valor != valor:
            pai = atual
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        if not atual:

            print('Elemento não encontrado.')
            return False
        
        if atual.esquerda and atual.direita:
            pai_sucessor = atual
            sucessor = atual.direita

            while sucessor.esquerda:
                pai_sucessor = sucessor
                sucessor = sucessor.esquerda

            atual.valor = sucessor.valor
            pai = pai_sucessor
            atual = sucessor

        filho = atual.esquerda or atual.direita
        if pai is None:
            self.raiz = filho
        elif pai.esquerda == atual:
            pai.esquerda = filho
        else:
            pai.direita = filho
        return True


    def buscar(self, valor):

        atual = self.raiz
        while atual:
            if valor == atual.valor:
                print(f'Valor encontrado: {valor}')
                return True
            if valor < atual.valor:
                atual = atual.esquerda

            else:
                atual = atual.direita
        print('Valor não encontrado!')
    def altura(self, no):
        if no is None:
            return 0
        alt_esquerda = self.altura(no.esquerda)
        alt_direita = self.altura(no.direita)
        return 1 + max(alt_esquerda, alt_direita)
    
    def para_grafo(self):
        grafo = {}
        def percorrer(no, pai):
            if no is None:
                return
            grafo[str(no.valor)] = []
            if pai is not None:
                grafo[str(no.valor)].append(str(pai.valor))
            if no.esquerda:
                grafo[str(no.valor)].append(str(no.esquerda.valor))
            if no.direita:
                grafo[str(no.valor)].append(str(no.direita.valor))

            percorrer(no.esquerda, no)
            percorrer(no.direita, no)
        percorrer(self.raiz, None)
        return grafo
            
    
    def preOrdem(self, no):
        if no is not None:
            print(no.valor)
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)

    def emOrdem(self, no):
        if no is not None:
            self.emOrdem(no.esquerda)
            print(no.valor)
            self.emOrdem(no.direita)
    
    def posOrdem(self, no):
        if no is not None:
            self.posOrdem(no.esquerda)
            self.posOrdem(no.direita)
            print(no.valor)
arvore = Tree()
valores = random.sample(range(1, 100), 20)

print(f'Valores presentes na árvore: {valores}')
for v in valores:
    arvore.inserir(v)

#Teste de arvore
print('\nPré-Ordem: ', end=' '); arvore.preOrdem(arvore.raiz)
print('\nEm-Ordem: ', end=' '); arvore.emOrdem(arvore.raiz)
print('\nPós-Ordem: ', end=' '); arvore.posOrdem(arvore.raiz)
print(f'\nAltura da Árvore: {arvore.altura(arvore.raiz)}')



if __name__ == '__main__':
    arvore = Tree()
    valores = random.sample(range(1, 100), 20)
    for v in valores:
        arvore.inserir(v)
    print(f'Valores: {valores}')