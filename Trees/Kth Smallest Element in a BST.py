from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        res = []

        def inorder(curr: Optional[TreeNode]):
            if not curr:
                return
            
            inorder(curr.left)
            res.append(curr.val)
            inorder(curr.right)
        
        inorder(root)
        return res[k-1]