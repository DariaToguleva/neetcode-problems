# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        dif = True
        def balance(node) -> int:
            nonlocal dif

            if not node:
                return -1

            left = balance(node.left)
            right = balance(node.right)

            if abs(left - right) > 1:
                dif = False

            return max(left, right) + 1
        balance(root)    
        return dif
        