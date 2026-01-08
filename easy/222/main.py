class Solution(object):
    def countNodes(self, root):
        if not root: return 0

        left_levels = 0
        left = root.left
        while left:
            left = left.left
            left_levels += 1

        right_levels = 0
        right = root.right
        while right:
            right = right.right
            right_levels += 1

        if left_levels == right_levels:
            return pow(2, right_levels + 1) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)