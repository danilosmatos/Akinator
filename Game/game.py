from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional, List, Tuple


@dataclass
class No:
    pergunta: Optional[str] = None
    resposta: Optional[str] = None
    sim: Optional["No"] = None
    nao: Optional["No"] = None

    def folha(self) -> bool:
        return self.resposta is not None


def criar_arvore() -> No:
    return No(resposta="Python")


def dfs(no: Optional[No]) -> None:
    if not no:
        return
    print(f"[DFS] {no.pergunta or 'RESPOSTA: ' + no.resposta}")
    dfs(no.sim); dfs(no.nao)


def bfs_personagens(raiz: No) -> List[str]:
    if not raiz:
        return []

    out: List[str] = []
    q = deque([raiz])
    while q:
        n = q.popleft()
        if n.folha():
            out.append(n.resposta) 
            continue
        if n.sim:
            q.append(n.sim)
        if n.nao:
            q.append(n.nao)
    return out


def caminho_bfs(raiz: No, alvo: str) -> List[Tuple[str, str]]:
    if not raiz:
        return []

    q: deque[Tuple[No, List[Tuple[str, str]]]] = deque([(raiz, [])])
    while q:
        n, path = q.popleft()
        if n.folha():
            if n.resposta == alvo:
                return path
            continue
        assert n.pergunta
        if n.sim:
            q.append((n.sim, path + [(n.pergunta, "s")]))
        if n.nao:
            q.append((n.nao, path + [(n.pergunta, "n")]))
    return []


class Akinator:
    def __init__(self):
        self.raiz = criar_arvore()
        self.rodadas = 0
        self.acertos = 0

    def _perguntar(self, p: str) -> bool:
        while True:
            r = input(p).strip().lower()
            if r in ("s", "sim"):
                return True
            if r in ("n", "não", "nao"):
                return False
            print(" Responda 's' ou 'n'.")

    def _jogar(self) -> None:
        no = self.raiz
        caminho: List[Tuple[No, bool]] = []
        while not no.folha():
            assert no.pergunta
            resp = self._perguntar(f" {no.pergunta} (s/n): ")
            caminho.append((no, resp))
            no = no.sim if resp else no.nao

        print(f"Você pensou em: {no.resposta.upper()}!")
        if self._perguntar("  Acertei? (s/n): "):
            self.acertos += 1
            print(" Sabia! Sou o Akinator!")
        else:
            self._aprender(no, caminho)

    def _aprender(self, errado: No, caminho: List[Tuple[No, bool]]) -> None:
        print("Errei! Me ensine...")
        novo = input("  Qual era o personagem? ").strip()
        perg = input(f"  Pergunta que diferencia '{novo}' de '{errado.resposta}'?\n  (sim = '{novo}'): ").strip()
        if not novo or not perg:
            return

        novo_no = No(pergunta=perg, sim=No(resposta=novo), nao=No(resposta=errado.resposta))
        if caminho:
            pai, resp = caminho[-1]
            if resp:
                pai.sim = novo_no
            else:
                pai.nao = novo_no
        else:
            self.raiz = novo_no
        print(f" Aprendi sobre '{novo}'!")

    def mostrar_arvore(self) -> None:
        print("\n Árvore (DFS):\n")
        dfs(self.raiz)

    def mostrar_personagens(self) -> None:
        pers = bfs_personagens(self.raiz)
        print(f" Personagens ({len(pers)}) — BFS:")
        for i, p in enumerate(pers, 1):
            print(f"     {i}. {p}")

    def mostrar_caminho(self) -> None:
        nome = input("  Personagem: ").strip()
        caminho = caminho_bfs(self.raiz, nome)
        if not caminho:
            print(f" '{nome}' não encontrado.")
            return
        print(f" Caminho até '{nome}':")
        for i, (q, r) in enumerate(caminho, 1):
            print(f"     {i}. {q} → {r}")

    def mostrar_stats(self) -> None:
        taxa = (self.acertos / self.rodadas * 100) if self.rodadas else 0
        print(f"\n  Rodadas: {self.rodadas} | Acertos: {self.acertos} | Taxa: {taxa:.1f}% | Personagens: {len(bfs_personagens(self.raiz))}")

    def run(self) -> None:
        print("\n   AKINATOR  ")
        self.mostrar_personagens()
        menu = {
            "1": self.iniciar,
            "2": self.mostrar_arvore,
            "3": self.mostrar_personagens,
            "4": self.mostrar_caminho,
            "5": self.mostrar_stats,
        }
        while True:
            print("\n  [1] Jogar  [2] Árvore  [3] Personagens  [4] Caminho  [5] Stats  [0] Sair")
            op = input("  > ").strip()
            if op == "0":
                print("  Até logo! ")
                break
            if op in menu:
                menu[op]()

    def iniciar(self) -> None:
        input("\n Pense em um personagem e pressione Enter...")
        self.rodadas += 1
        self._jogar()


if __name__ == "__main__":
    Akinator().run()
