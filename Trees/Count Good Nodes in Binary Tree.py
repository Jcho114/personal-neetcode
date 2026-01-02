from typing import Optional
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        def helper(curr: Optional[TreeNode], maximum: int) -> int:
            if not curr:
                return 0
            
            maximum = max(maximum, curr.val)
            left, right = helper(curr.left, maximum), helper(curr.right, maximum)
            return left + right + (1 if curr.val >= maximum else 0)

        return helper(root, -inf)