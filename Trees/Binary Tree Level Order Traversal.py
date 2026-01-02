from typing import Optional, List
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        TC: O(n)
        SC: O(n)
        """
        queue = deque([(0, root)])
        levels = defaultdict(list)

        while queue:
            level, node = queue.popleft()
            if node:
                levels[level].append(node.val)
                queue.append((level+1, node.left))
                queue.append((level+1, node.right))

        return list(levels.values())