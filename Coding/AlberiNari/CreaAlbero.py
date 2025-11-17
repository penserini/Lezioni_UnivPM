from __future__ import annotations
from dataclasses import dataclass, field
from typing import Generic, List, Iterable, TypeVar, Deque, Callable
from collections import deque

T = TypeVar("T")

@dataclass
class NaryNode(Generic[T]):
    """
    Generic[T] dice: “questa classe è generica sul tipo T”.
    value: T e children: List[NaryNode[T]] significano che tutti i valori 
    del nodo e dei suoi figli hanno lo stesso tipo.
    """
    value: T
    
    """
    Il default_factory=list garantisce che ogni nodo abbia la sua lista separata, 
    e non una lista condivisa da tutti i nodi.
    """
    children: List["NaryNode[T]"] = field(default_factory=list)

    # -- costruzione albero --
    # add_child => nodo foglia
    def add_child(self, value: T) -> "NaryNode[T]":
        child = NaryNode(value)
        self.children.append(child)
        return child

    # add_children => lista di nodi associata un singolo nodo
    def add_children(self, values: Iterable[T]) -> List["NaryNode[T]"]:
        nodes = [NaryNode(v) for v in values]
        # aggiunge questi nuovi nodi "nodes" alla lista dei figli del nodo corrente "self".
        self.children.extend(nodes) 
        return nodes

    # -- visite --
    def dfs_preorder(self):                
        yield self    
        
        for c in self.children:
            yield from c.dfs_preorder()

    def bfs(self):
        q: Deque[NaryNode[T]] = deque([self])
        while q:
            node = q.popleft()
            yield node
            q.extend(node.children)
    
    # stampa dei nodi visitati senza usare "yield"
    def print_dfs_preorder(self):
        """Stampa i nodi in ordine DFS-preorder: Nodo -> Figli"""
        print(f"Visito nodo: {self.value}")
        for c in self.children:
            c.print_dfs_preorder()
    
    def print_dfs_postorder(self):
        """Stampa i nodi in ordine DFS-postorder: Figli -> Nodo"""
        for c in self.children:
            c.print_dfs_postorder()
        print(f"Visito nodo: {self.value}")

    def print_bfs(self):
        """Stampa i nodi in ordine BFS (livelli)"""
        q: Deque[NaryNode[T]] = deque([self]) # q è una coda doppia (double-ended queue), 
                                              # che conterrà elementi di tipo NaryNode[T]
        while q:
            node = q.popleft()
            print(f"Visito nodo: {node.value}")
            q.extend(node.children)

    # -- stampa carina --
    def render(
        self,
        to_str: Callable[[T], str] = str,
        *,
        unicode: bool = True,
        show_root: bool = True
    ) -> str:
        if unicode:
            branch_mid, branch_last, pipe, space = "├── ", "└── ", "│   ", "    "
        else:
            branch_mid, branch_last, pipe, space = "+-- ", "+-- ", "|   ", "    "

        lines: List[str] = []

        def _render_subtree(node: "NaryNode[T]", prefix: str, is_last: bool):
            connector = branch_last if is_last else branch_mid
            lines.append(f"{prefix}{connector}{to_str(node.value)}")
            new_prefix = prefix + (space if is_last else pipe)
            last_idx = len(node.children) - 1
            for i, ch in enumerate(node.children):
                _render_subtree(ch, new_prefix, i == last_idx)

        if show_root:
            lines.append(to_str(self.value))
            last_idx = len(self.children) - 1
            for i, ch in enumerate(self.children):
                _render_subtree(ch, "", i == last_idx)
        else:
            last_idx = len(self.children) - 1
            for i, ch in enumerate(self.children):
                _render_subtree(ch, "", i == last_idx)

        return "\n".join(lines)


# ---- esempio d'uso ----
if __name__ == "__main__":
    root = NaryNode("A")
    b, c, d = root.add_children(["B", "C", "D"])
    b.add_children(["E", "F"])
    g = c.add_child("G")
    g.add_children(["I", "L"])
    d.add_child("H")

    print("Stampa dell'albero creato con la funzione render():")
    print(root.render(unicode=True))

    print("\nStampa con print_dfs_preorder():")
    root.print_dfs_preorder()

    print("\nStampa con print_dfs_postorder():")
    root.print_dfs_postorder()

    print("\nStampa con print_bfs():")
    root.print_bfs()

