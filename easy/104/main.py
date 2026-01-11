class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)

        return 1 + max(right, left)