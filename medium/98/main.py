# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inner(node, left, right):
            if not node:
                return True

            value = node.val
            
            if not (value > left and value < right):
                return False

            return inner(node.left, left, value) and inner(node.right, value, right)

        return inner(root, float("-inf"), float("inf"))