from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        def helper(curr: Optional[TreeNode]) -> Tuple[int, bool]:
            if not curr:
                return 0, True
            left, right = helper(curr.left), helper(curr.right)
            if not left[1] or not right[1]:
                return 0, False
            if abs(left[0] - right[0]) > 1:
                return 0, False
            depth = 1 + max(left[0], right[0])
            return depth, True
        return helper(root)[1]