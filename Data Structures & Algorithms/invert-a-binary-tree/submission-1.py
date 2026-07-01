# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.help(root)

    def help(self, node: Optional[TreeNode]):
        if node is None:
            return None
        self.help(node.left)
        self.help(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp
        return node

