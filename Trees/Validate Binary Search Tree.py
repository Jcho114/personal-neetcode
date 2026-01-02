from typing import Optional
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        def helper(curr: Optional[TreeNode], mn: int, mx: int) -> bool:
            if not curr:
                return True

            return (
                mn < curr.val < mx and
                helper(curr.left, mn, curr.val) and
                helper(curr.right, curr.val, mx)
            )

        return helper(root, -inf, inf)