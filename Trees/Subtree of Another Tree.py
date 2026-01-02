from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        TC: O(N + M)
        SC: O(N + M)
        """
        def serialize(curr: Optional[TreeNode]) -> str:
            if not curr:
                return "$#"
            return f"${curr.val}{serialize(curr.left)}{serialize(curr.right)}"
        
        rootStr, subRootStr = serialize(root), serialize(subRoot)
        return subRootStr in rootStr