from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        TC: O(V * IACK(V))
        SC: O(V)
        """
        parents = [i for i in range(n)]
        ranks = [0]*n

        def parent(a: int) -> int:
            if parents[a] != a:
                parents[a] = parent(parents[a])
            return parents[a]

        def merge(a: int, b: int):
            pa, pb = parent(a), parent(b)
            if ranks[pa] > ranks[pb]:
                parents[pb] = pa
                ranks[pa] += ranks[pb]
            else:
                parents[pa] = pb
                ranks[pb] += ranks[pa]
        
        for src, dst in edges:
            if parent(src) == parent(dst):
                return False
            merge(src, dst)

        return len(set(parent(node) for node in range(n))) == 1