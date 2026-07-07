# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def help(node, count, maximum) -> int:
            if node is None:
                return maximum
            count += 1
            if count > maximum:
                maximum = count
            maxR = help(node.right, count, maximum)
            maxL = help(node.left, count, maximum) 
            return max(maxR, maxL) 
        return help(root, 0, 0)    
