# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def comp(nodeP, nodeQ) -> bool:
            if nodeP is None and nodeQ is None:
                return True
            if nodeP is None or nodeQ is None:
                return False
            if nodeP.val != nodeQ.val:
                return False   
            p = comp(nodeP.left, nodeQ.left)
            q = comp(nodeP.right, nodeQ.right)     
            return p and q
        return comp(p, q)    