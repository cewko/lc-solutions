class Solution(object):
    def isSymmetric(self, root):
        def inner(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val == right.val and
            inner(left.left, right.right) and
            inner(left.right, right.left))

        return inner(root.left, root.right)


from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True
