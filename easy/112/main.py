class Solution(object):
    def hasPathSum(self, root, targetSum):
        def inner(root, current_value):
            if not root:
                return False

            current_value += root.val
            if not root.left and not root.right:
                return current_value == targetSum

            return inner(root.left, current_value) or inner(root.right, current_value)

        return inner(root, 0)


from collections import deque

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            root, current_value = queue.popleft()

            if not root.left and not root.right:
                if current_value == targetSum:
                    return True

            if root.left:
                queue.append([root.left, current_value + root.left.val])
            if root.right:
                queue.append([root.right, current_value + root.right.val])

        return False
