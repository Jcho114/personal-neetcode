from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        TC: O(n)
        SC: O(d)
        """
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            for _ in range(len(queue)-1):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            right = queue.popleft()
            res.append(right.val)

            if right.left: queue.append(right.left)
            if right.right: queue.append(right.right)
        
        return res