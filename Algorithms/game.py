from tree import ArvoreDecisao
from bfs import bfs
from dfs import dfs


class Akinator:
    def __init__(self):
        self.arvore = ArvoreDecisao()
        self.raiz = self.arvore.raiz

    def perguntar(self, texto):
        while True:
            resp = input(f"{texto} (s/n): ").strip().lower()
            if resp in ["s", "sim"]:
                return True
            elif resp in ["n", "nao", "não"]:
                return False
            else:
                print("Responda apenas com 's' ou 'n'.")

    # -------------------------
    # JOGO PRINCIPAL
    # -------------------------
    def jogar(self):
        no = self.raiz
        caminho = []

        while True:
            # Se for folha → resposta final
            if no.resposta:
                print(f"\nVocê pensou em: {no.resposta}?")

                acertou = self.perguntar("Acertei?")
                if not acertou:
                    self.aprender(no, caminho)
                else:
                    print("Acertei.")
                return

            # Se for pergunta
            resposta = self.perguntar(no.pergunta)
            caminho.append((no, resposta))

            if resposta:
                no = no.yes
            else:
                no = no.no

    # -------------------------
    # APRENDIZADO
    # -------------------------
    def aprender(self, no_errado, caminho):
        print("\nNão sei então. Me ensine.")

        novo = input("Qual era o correto? ").strip()
        pergunta = input(
            f"Digite uma pergunta que diferencie '{novo}' de '{no_errado.resposta}': "
        ).strip()

        if not novo or not pergunta:
            print("Entrada inválida. Abortando aprendizado.")
            return

        nova_pergunta = no_errado.__class__(pergunta=pergunta)
        nova_pergunta.yes = no_errado.__class__(resposta=novo)
        nova_pergunta.no = no_errado.__class__(resposta=no_errado.resposta)

        # ligar ao pai
        if caminho:
            pai, resp = caminho[-1]
            if resp:
                pai.yes = nova_pergunta
            else:
                pai.no = nova_pergunta
        else:
            # caso raiz
            self.raiz = nova_pergunta

        print("Aprendi algo novo.")

    # -------------------------
    # VISUALIZAÇÕES (REQUISITO)
    # -------------------------
    def mostrar_bfs(self):
        print("\n--- BFS (ordem de visita) ---")
        ordem = bfs(self.raiz)
        for i, item in enumerate(ordem, 1):
            print(f"{i}. {item}")

    def mostrar_dfs(self):
        print("\n--- DFS (ordem de visita) ---")
        dfs(self.raiz)
