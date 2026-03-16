class Node:
    def __init__(self, question=None, answer=None):
        self.question = question  # Nó interno
        self.answer = answer      # Nó folha (animal)
        self.yes = None           # Lado Esquerdo
        self.no = None            # Lado Direito

def run_dfs(node):
  if node is None:
      return
    
  valor = node.question if node.question else f"RESPOSTA: {node.answer}"
  print(f"[DFS Visita]: {valor}")
    
  run_dfs(node.yes)
  run_dfs(node.no)
