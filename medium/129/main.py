# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        def inner(cur_node, sum_num):
            if not cur_node:
                return 0

            sum_num = sum_num * 10 + cur_node.val
            if not cur_node.left and not cur_node.right:
                return sum_num

            return inner(cur_node.left, sum_num) + inner(cur_node.right, sum_num)

        return inner(root, 0)