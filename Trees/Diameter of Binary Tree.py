from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        res = 0

        def helper(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0

            nonlocal res
            left, right = helper(curr.left), helper(curr.right)
            res = max(res, left+right)
            return 1 + max(left, right)
        
        helper(root)
        return res