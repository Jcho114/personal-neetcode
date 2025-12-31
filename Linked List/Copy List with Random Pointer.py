from typing import Optional, Self

class Node:
    def __init__(self, x: int, next: Self = None, random: Self = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        TC: O(n)
        SC: O(n)
        """
        clones = {None: None}
    
        def clone(curr: Optional[Node]) -> Optional[Node]:
            if curr in clones:
                return clones[curr]
            clones[curr] = Node(curr.val)
            clones[curr].next = clone(curr.next)
            clones[curr].random = clone(curr.random)
            return clones[curr]

        return clone(head)