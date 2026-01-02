from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        TC: O(n)
        SC: O(h)
        """
        def helper(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr:
                return
            curr.left, curr.right = curr.right, curr.left
            helper(curr.left)
            helper(curr.right)

        helper(root)
        return root