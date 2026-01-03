from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        TC: O(V + E*IACK(V))
        SC: O(V)
        """
        nodes = set()
        for src, dest in edges:
            nodes.add(src)
            nodes.add(dest)
        n = len(nodes)
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def parent(node):
            if parents[node] != node:
                parents[node] = parent(parents[node])
            return parents[node]

        def merge(node1, node2):
            pnode1, pnode2 = parent(node1), parent(node2)
            if ranks[pnode1] > ranks[pnode2]:
                parents[pnode2] = pnode1
                ranks[pnode1] += ranks[pnode2]
            else:
                parents[pnode1] = parent(pnode2)
                ranks[pnode2] += ranks[pnode1]

        for src, dest in edges:
            if parent(src-1) == parent(dest-1):
                return [src, dest]
            merge(src-1, dest-1)