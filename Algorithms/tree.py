from node import Node
class ArvoreDecisao:

    def __init__(self):
        self.raiz = self.montar_arvore()

    def montar_arvore(self):
        raiz = Node(pergunta = 'Vive na água?') #raiz

        raiz.yes = Node(pergunta = 'É mamífero? ')
        raiz.no = Node(pergunta = 'Tem asas?')

        #caso a raiz seja sim

        raiz.yes.yes = Node(pergunta = 'É um Golfinho?')
        raiz.yes.no = Node(pergunta = 'É um Tubarão?')

        #caso a raiz seja não

        raiz.no.yes = Node(pergunta = 'É uma animal aéreo? ')
        raiz.no.no = Node(pergunta = 'Tem quatro patas? ')

        raiz.no.yes.yes = Node(resposta = 'É uma Águia?')
        raiz.no.yes.no = Node(resposta = 'É um Pinguim?')

        raiz.no.no.yes = Node(resposta = 'É um cachorro?')
        raiz.no.no.no = Node(resposta = 'É uma cobra?')

        return raiz

