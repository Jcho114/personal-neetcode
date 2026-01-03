from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        TC: O(V+E)
        SC: O(V)
        """
        clones = {None: None}

        def clone(curr: Optional[Node]) -> Optional[Node]:
            if curr in clones:
                return clones[curr]
            clones[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                clones[curr].neighbors.append(clone(neighbor))
            return clones[curr]

        return clone(node)