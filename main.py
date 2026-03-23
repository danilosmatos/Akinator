from Algorithms.game import Akinator
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs

def mostrar_menu():
    print("\nMENU\n")
    print("1 - Jogar")
    print("2 - Comparar BFS x DFS")
    print("0 - Sair")

def comparar(arvore):
    print("\n--- Árvore de Decisão: Akinator ---")
    print("                  Vive na água?")
    print("                 /             \\")
    print("               Sim             Não")
    print("              /   \\           /   \\")
    print("      É mamífero?           Tem asas?")
    print("       /      \\             /      \\")
    print("   Golfinho  Tubarão      Aéreo?    4 Patas?")
    print("                          /   \\      /    \\")
    print("                      Águia Pinguim Cachorro Cobra")

    bfs_ordem = bfs(arvore.raiz)
    dfs_ordem = dfs(arvore.raiz)

    print("\n--- BFS ---")
    for i, no in enumerate(bfs_ordem, 1):
        print(f"{i}. {no}")

    print("\n--- DFS ---")
    for i, no in enumerate(dfs_ordem, 1):
        print(f"{i}. {no}")

    print("\nComparação:\n")

    print("Ordem de visita:")
    print("BFS percorre nível por nível.")
    print("DFS percorre aprofundando primeiro.")

    print("\nQuantidade de nós visitados:")
    print(f"BFS: {len(bfs_ordem)} nós")
    print(f"DFS: {len(dfs_ordem)} nós")

    print("\nComplexidade:")
    print("BFS: O(n) tempo | O(n) memória")
    print("DFS: O(n) tempo | O(h) memória")

    print("\nComportamento:")
    print("BFS avalia várias possibilidades por nível.")
    print("DFS segue um caminho até o fim antes de voltar.")

def main():
    jogo = Akinator()
    arvore = jogo.arvore

    while True:
        mostrar_menu()
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            jogo.jogar()

        elif op == "2":
            comparar(arvore)

        elif op == "0":
            print("Encerrando.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()