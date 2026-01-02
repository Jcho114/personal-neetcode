from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        TC: O(n)
        SC: O(1)
        """
        less, greater = (p.val, q.val) if p.val <= q.val else (q.val, p.val)
        curr = root

        while curr:
            if less <= curr.val <= greater:
                return curr
            
            if curr.val > greater:
                curr = curr.left
            else:
                curr = curr.right
        
        return None