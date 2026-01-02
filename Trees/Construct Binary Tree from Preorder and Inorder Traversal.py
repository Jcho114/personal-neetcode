from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        TC: O(n)
        SC: O(n)
        """
        preorder.reverse()
        def helper(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None

            divider = preorder.pop()
            i = l
            while i <= r and inorder[i] != divider:
                i += 1
            left = helper(l, i-1)
            right = helper(i+1, r)

            return TreeNode(divider, left, right)
        
        return helper(0, len(inorder)-1)