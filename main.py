from Algorithms.game import Akinator
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.tree import ArvoreDecisao


def mostrar_menu():
    print("\nMENU\n")
    print("1 - Jogar")
    print("2 - Mostrar BFS")
    print("3 - Mostrar DFS")
    print("0 - Sair")


def executar_bfs(arvore):
    print("\n--- BFS (Busca em Largura) ---")
    ordem = bfs(arvore.raiz)

    for i, no in enumerate(ordem, 1):
        print(f"{i}. {no}")


def executar_dfs(arvore):
    print("\n--- DFS (Busca em Profundidade) ---")
    dfs(arvore.raiz)

def main():
    jogo = Akinator()
    arvore = ArvoreDecisao()

    while True:
        mostrar_menu()
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            jogo.jogar()

        elif op == "2":
            executar_bfs(arvore)

        elif op == "3":
            executar_dfs(arvore)

        elif op == "0":
            print("Encerrando.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()