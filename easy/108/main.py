class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def inner(left, right):
            if left > right:
                return None

            middle = (left + right) // 2
            root = TreeNode(nums[middle])

            root.left = inner(left, middle - 1)
            root.right = inner(middle + 1, right)

            return root

        return inner(0, len(nums) - 1)